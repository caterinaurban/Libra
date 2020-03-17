"""
Forward Analysis Engine
=======================

:Author: Caterina Urban
"""
from copy import deepcopy
from queue import Queue
from typing import Dict, Tuple

from apronpy.coeff import PyMPQScalarCoeff
from apronpy.lincons0 import ConsTyp
from apronpy.manager import PyManager
from apronpy.scalar import PyMPQScalar
from apronpy.tcons1 import PyTcons1, PyTcons1Array
from apronpy.texpr0 import TexprOp, TexprRtype, TexprRdir, TexprDiscr
from apronpy.texpr1 import PyTexpr1
from apronpy.var import PyVar

from libra.abstract_domains.deeppoly_domain import DeepPolyState
from libra.core.statements import Call
from libra.engine.interpreter import Interpreter
from libra.semantics.forward import DefaultForwardSemantics

from libra.abstract_domains.state import State
from libra.core.cfg import Node, Function, Activation


rtype = TexprRtype.AP_RTYPE_REAL
rdir = TexprRdir.AP_RDIR_RND


# def texpr_to_dict(texpr):
#
#     def do(texpr0, env):
#         if texpr0.discr == TexprDiscr.AP_TEXPR_CST:
#             result = dict()
#             t0 = '{}'.format(texpr0.val.cst)
#             t1 = eval(t0)
#             t2 = str(t1)
#             t3 = float(t2)
#             result['_'] = t3
#             return result
#         elif texpr0.discr == TexprDiscr.AP_TEXPR_DIM:
#             result = dict()
#             result['{}'.format(env.var_of_dim[texpr0.val.dim.value].decode('utf-8'))] = 1.0
#             return result
#         else:
#             assert texpr0.discr == TexprDiscr.AP_TEXPR_NODE
#             left = do(texpr0.val.node.contents.exprA.contents, env)
#             op = texpr0.val.node.contents.op
#             if texpr0.val.node.contents.exprB:
#                 right = do(texpr0.val.node.contents.exprB.contents, env)
#             if op == TexprOp.AP_TEXPR_ADD:
#                 result = deepcopy(left)
#                 for var, val in right.items():
#                     if var in result:
#                         result[var] += val
#                     else:
#                         result[var] = val
#                 return result
#             elif op == TexprOp.AP_TEXPR_SUB:
#                 result = deepcopy(left)
#                 for var, val in right.items():
#                     if var in result:
#                         result[var] -= val
#                     else:
#                         result[var] = -val
#                 return result
#             elif op == TexprOp.AP_TEXPR_MUL:
#                 # print('multiplying')
#                 # print('left: ', left)
#                 # print('right: ', right)
#                 result = dict()
#                 if '_' in left and len(left) == 1:
#                     for var, val in right.items():
#                         result[var] = left['_'] * right[var]
#                 elif '_' in right and len(right) == 1:
#                     for var, val in left.items():
#                         result[var] = right['_'] * left[var]
#                 else:
#                     assert False
#                 # print('result: ', result)
#             elif op == TexprOp.AP_TEXPR_NEG:
#                 result = deepcopy(left)
#                 for var, val in result.items():
#                     result[var] = -val
#         return result
#
#     texpr1 = texpr.texpr1.contents
#     return do(texpr1.texpr0.contents, texpr1.env.contents)
#
#
# def substitute_in_dict(todict, var, rhs):
#     result = todict
#     key = str(var)
#     coeff = result[key]
#     del result[key]
#     for var, val in rhs.items():
#         if var in result:
#             result[var] += coeff * val
#         else:
#             result[var] = coeff * val
#     return result
#
#
# def dict_to_texpr(todict, env):
#     texpr = PyTexpr1.cst(env, PyMPQScalarCoeff(PyMPQScalar(todict['_'])))
#     for var, val in reversed(list(todict.items())):
#         if var != '_':
#             coeff = PyTexpr1.cst(env, PyMPQScalarCoeff(PyMPQScalar(val)))
#             dim = PyTexpr1.var(env, PyVar(var))
#             term = PyTexpr1.binop(TexprOp.AP_TEXPR_MUL, coeff, dim, TexprRtype.AP_RTYPE_REAL, TexprRdir.AP_RDIR_RND)
#             texpr = PyTexpr1.binop(TexprOp.AP_TEXPR_ADD, term, texpr, TexprRtype.AP_RTYPE_REAL, TexprRdir.AP_RDIR_RND)
#     return texpr


class ForwardInterpreter(Interpreter):
    """Forward control flow graph interpreter."""

    def __init__(self, cfg, manager: PyManager, semantics, widening=3, symbolic1=False, symbolic2=False):
        """Forward control flow graph interpreter construction.

        :param cfg: control flow graph to analyze
        :param semantics: semantics of statements in the control flow graph
        :param widening: number of iterations before widening
        :param precursory: precursory control flow graph interpreter
        """
        super().__init__(cfg, semantics, widening)
        self.manager = manager
        self.symbolic1 = symbolic1
        self.symbolic2 = symbolic2

    def analyze(self, initial: DeepPolyState, earlystop=True, forced_active=None, forced_inactive=None, outputs=None):
        """Forward analysis extracting abstract activation patterns.

        :param initial: initial state of the analysis
        :return: three sets: all activation nodes, always active nodes, always inactive nodes
        """
        worklist = Queue()
        worklist.put(self.cfg.in_node)
        state = deepcopy(initial)
        activated, deactivated = set(), set()
        symbols: Dict[str, Tuple[PyVar, PyTexpr1]] = dict()
        unknowns = 0

        while not worklist.empty():
            current: Node = worklist.get()  # retrieve the current node
            # execute block
            if isinstance(current, Function):
                # print(state)
                state = state.affine(current.stmts[0], current.stmts[1])
                # print(state)
            elif isinstance(current, Activation):
                if forced_active and current in forced_active:
                    state = state.relu(current.stmts, active=True)
                elif forced_inactive and current in forced_inactive:
                    state = state.relu(current.stmts, inactive=True)
                else:
                    state = state.relu(current.stmts)
                    if state.is_bottom():
                        deactivated.add(current)
                    if state.flag:
                        if state.flag > 0:
                            activated.add(current)
                        else:
                            deactivated.add(current)
            else:
                for stmt in reversed(current.stmts):
                    state = self.semantics.assume_call_semantics(stmt, state, self.manager)
            # update worklist
            for node in self.cfg.successors(current):
                worklist.put(self.cfg.nodes[node.identifier])

        found = None
        if state.is_bottom():
            found = '⊥'
        else:
            for chosen in outputs:
                outcome = state.bounds[chosen.name]
                lower = outcome.lower
                unique = True
                remaining = outputs - {chosen}
                for discarded in remaining:
                    alternative = state.bounds[discarded.name]
                    upper = alternative.upper
                    if lower <= upper:
                        unique = False
                        break
                if unique:
                    found = chosen
                    break

        return activated, deactivated, found


class ActivationPatternForwardSemantics(DefaultForwardSemantics):

    def assume_call_semantics(self, stmt: Call, state: State, manager: PyManager = None) -> State:
        argument = self.semantics(stmt.arguments[0], state).result
        state.assume(argument)
        state.result = set()
        return state

    def list_semantics(self, stmt, state) -> State:
        state = state.affine(stmt[0], stmt[1])
        return state

    def ReLU_call_semantics(self, stmt, state, manager: PyManager = None, active: bool = True) -> State:
        assert manager is not None
        if active:  # assume h >= 0
            expr = PyTexpr1.var(state.environment, stmt)
            cond = PyTcons1.make(expr, ConsTyp.AP_CONS_SUPEQ)
            abstract1 = state.domain(manager, state.environment, array=PyTcons1Array([cond]))
            state.state = state.state.meet(abstract1)
            return state
        else:  # assume h < 0, assign h = 0
            expr = PyTexpr1.var(state.environment, stmt)
            neg = PyTexpr1.unop(TexprOp.AP_TEXPR_NEG, expr, rtype, rdir)
            cond = PyTcons1.make(neg, ConsTyp.AP_CONS_SUP)
            abstract1 = state.domain(manager, state.environment, array=PyTcons1Array([cond]))
            zero = PyTexpr1.cst(state.environment, PyMPQScalarCoeff(0.0))
            state.state = state.state.meet(abstract1).assign(stmt, zero)
            return state
