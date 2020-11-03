"""
Reduced Product of Intervals+Symbolic Constant Propagation (Version 2) and DeepPoly
===================================================================================

:Authors: Caterina Urban
"""
import time
from copy import deepcopy
from math import inf
from typing import Set, List, Dict, Tuple

from apronpy.manager import PyManager
from apronpy.texpr0 import TexprRtype, TexprRdir, TexprDiscr, TexprOp
from apronpy.texpr1 import PyTexpr1
from apronpy.var import PyVar

from libra.abstract_domains.deeppoly_domain import IntervalLattice
from libra.abstract_domains.state import State
from libra.core.expressions import VariableIdentifier, Expression, BinaryBooleanOperation, \
    BinaryComparisonOperation, Literal, UnaryArithmeticOperation
from libra.core.utils import copy_docstring


rtype = TexprRtype.AP_RTYPE_REAL
rdir = TexprRdir.AP_RDIR_RND


def texpr_to_dict(texpr):

    def do(texpr0, env):
        if texpr0.discr == TexprDiscr.AP_TEXPR_CST:
            result = dict()
            t0 = '{}'.format(texpr0.val.cst)
            t1 = eval(t0)
            t2 = str(t1)
            t3 = float(t2)
            result['_'] = t3
            return result
        elif texpr0.discr == TexprDiscr.AP_TEXPR_DIM:
            result = dict()
            result['{}'.format(env.var_of_dim[texpr0.val.dim.value].decode('utf-8'))] = 1.0
            return result
        else:
            assert texpr0.discr == TexprDiscr.AP_TEXPR_NODE
            left = do(texpr0.val.node.contents.exprA.contents, env)
            op = texpr0.val.node.contents.op
            if texpr0.val.node.contents.exprB:
                right = do(texpr0.val.node.contents.exprB.contents, env)
            if op == TexprOp.AP_TEXPR_ADD:
                result = deepcopy(left)
                for var, val in right.items():
                    if var in result:
                        result[var] += val
                    else:
                        result[var] = val
                return result
            elif op == TexprOp.AP_TEXPR_SUB:
                result = deepcopy(left)
                for var, val in right.items():
                    if var in result:
                        result[var] -= val
                    else:
                        result[var] = -val
                return result
            elif op == TexprOp.AP_TEXPR_MUL:
                # print('multiplying')
                # print('left: ', left)
                # print('right: ', right)
                result = dict()
                if '_' in left and len(left) == 1:
                    for var, val in right.items():
                        result[var] = left['_'] * right[var]
                elif '_' in right and len(right) == 1:
                    for var, val in left.items():
                        result[var] = right['_'] * left[var]
                else:
                    assert False
                # print('result: ', result)
            elif op == TexprOp.AP_TEXPR_NEG:
                result = deepcopy(left)
                for var, val in result.items():
                    result[var] = -val
        return result

    texpr1 = texpr.texpr1.contents
    return do(texpr1.texpr0.contents, texpr1.env.contents)


def evaluate(dictionary, bounds):
    result = IntervalLattice(0, 0)
    for var, val in dictionary.items():
        coeff = IntervalLattice(val, val)
        if var != '_':
            result = result._add(coeff._mult(bounds[var]))
        else:
            result = result._add(coeff)
    return result


def substitute_in_dict(todict, var, rhs):
    result = todict
    key = str(var)
    coeff = result[key]
    del result[key]
    for var, val in rhs.items():
        if var in result:
            result[var] += coeff * val
        else:
            result[var] = coeff * val
    return result


class ProductState(State):
    """Interval+Symbolic (Variant 2)+DeepPoly

    .. document private methods
    .. automethod:: ProductState._assign
    .. automethod:: ProductState._assume
    .. automethod:: ProductState._output
    .. automethod:: ProductState._substitute

    """
    def __init__(self, inputs: Set[VariableIdentifier], precursory: State = None):
        super().__init__(precursory=precursory)
        self.inputs = {input.name for input in inputs}
        self.bounds: Dict[str, IntervalLattice] = dict()
        for input in self.inputs:
            self.bounds[input] = IntervalLattice(0, 1)
        self.poly = dict()
        for input in self.inputs:
            _inf: Dict[str, float] = dict()
            _inf['_'] = 0.0
            _sup: Dict[str, float] = dict()
            _sup['_'] = 1.0
            self.poly[input] = (_inf, _sup)
        self.symbols: Dict[str, Tuple[str, dict]] = dict()
        self.flag = None

    @copy_docstring(State.bottom)
    def bottom(self):
        for var in self.bounds:
            self.bounds[var].bottom()
        return self

    @copy_docstring(State.top)
    def top(self):
        for var in self.bounds:
            self.bounds[var].top()
        return self

    def __repr__(self):
        items = sorted(self.bounds.items(), key=lambda x: x[0])
        return ", ".join("{} -> {}".format(variable, value) for variable, value in items)

    @copy_docstring(State.is_bottom)
    def is_bottom(self) -> bool:
        return any(element.is_bottom() for element in self.bounds.values())

    @copy_docstring(State.is_top)
    def is_top(self) -> bool:
        return all(element.is_top() for element in self.bounds.values())

    @copy_docstring(State._less_equal)
    def _less_equal(self, other: 'ProductState') -> bool:
        raise NotImplementedError(f"Call to _is_less_equal is unexpected!")

    @copy_docstring(State._join)
    def _join(self, other: 'ProductState') -> 'ProductState':
        for var in self.bounds:
            self.bounds[var].join(other.bounds[var])
            bounds = self.bounds[var]
            inf: Dict[str, float] = dict()
            inf['_'] = bounds.lower
            sup: Dict[str, float] = dict()
            sup['_'] = bounds.upper
            self.poly[var] = (inf, sup)
        return self

    @copy_docstring(State._meet)
    def _meet(self, other: 'ProductState') -> 'ProductState':
        for var in self.bounds:
            self.bounds[var].meet(other.bounds[var])
            bounds = self.bounds[var]
            _inf: Dict[str, float] = dict()
            _inf['_'] = bounds.lower
            sup: Dict[str, float] = dict()
            sup['_'] = bounds.upper
            self.poly[var] = (_inf, sup)
        return self

    @copy_docstring(State._widening)
    def _widening(self, other: 'ProductState') -> 'ProductState':
        raise NotImplementedError(f"Call to _widening is unexpected!")

    @copy_docstring(State._assign)
    def _assign(self, left: Expression, right: Expression) -> 'ProductState':
        raise NotImplementedError(f"Call to _assign is unexpected!")

    @copy_docstring(State._assume)
    def _assume(self, condition: Expression, bwd: bool = False) -> 'ProductState':
        raise NotImplementedError(f"Call to _assume is unexpected!")

    def assume(self, condition, manager: PyManager = None, bwd: bool = False) -> 'ProductState':
        if self.is_bottom():
            return self
        if isinstance(condition, tuple):
            condition = list(condition)
        if isinstance(condition, list):
            for feature, (lower, upper) in condition:
                self.bounds[feature.name].meet(IntervalLattice(lower, upper))
                bounds = self.bounds[feature.name]
                _inf: Dict[str, float] = dict()
                _inf['_'] = bounds.lower
                sup: Dict[str, float] = dict()
                sup['_'] = bounds.upper
                self.poly[feature.name] = (_inf, sup)
            return self
        elif isinstance(condition, BinaryBooleanOperation):
            if condition.operator == BinaryBooleanOperation.Operator.Or:
                right = deepcopy(self).assume(condition.right, bwd=bwd)
                return self.assume(condition.left, bwd=bwd).join(right)
            elif condition.operator == BinaryBooleanOperation.Operator.And:
                assert isinstance(condition.left, BinaryComparisonOperation)
                assert isinstance(condition.right, BinaryComparisonOperation)
                if isinstance(condition.left.left, Literal):
                    lower = eval(condition.left.left.val)
                else:
                    assert isinstance(condition.left.left, UnaryArithmeticOperation)
                    assert condition.left.left.operator == UnaryArithmeticOperation.Operator.Sub
                    assert isinstance(condition.left.left.expression, Literal)
                    lower = -eval(condition.left.left.expression.val)
                assert condition.left.operator == BinaryComparisonOperation.Operator.LtE
                assert isinstance(condition.left.right, VariableIdentifier)
                assert isinstance(condition.right.left, VariableIdentifier)
                assert condition.right.operator == BinaryComparisonOperation.Operator.LtE
                if isinstance(condition.right.right, Literal):
                    upper = eval(condition.right.right.val)
                else:
                    assert isinstance(condition.right.right, UnaryArithmeticOperation)
                    assert condition.right.right.operator == UnaryArithmeticOperation.Operator.Sub
                    assert isinstance(condition.right.right.expression, Literal)
                    upper = -eval(condition.right.right.expression.val)
                assert condition.left.right.name == condition.right.left.name
                self.bounds[condition.left.right.name].meet(IntervalLattice(lower, upper))
                bounds = self.bounds[condition.left.right.name]
                _inf: Dict[str, float] = dict()
                _inf['_'] = bounds.lower
                sup: Dict[str, float] = dict()
                sup['_'] = bounds.upper
                self.poly[condition.right.left.name] = (_inf, sup)
                return self
        elif isinstance(condition, BinaryComparisonOperation):
            if condition.operator == BinaryComparisonOperation.Operator.Gt:
                assert isinstance(condition.left, VariableIdentifier)
                assert isinstance(condition.right, Literal)
                lower = eval(condition.right.val)
                upper = inf
                self.bounds[condition.left.name].meet(IntervalLattice(lower, upper))
                bounds = self.bounds[condition.left.name]
                _inf: Dict[str, float] = dict()
                _inf['_'] = bounds.lower
                sup: Dict[str, float] = dict()
                sup['_'] = bounds.upper
                self.poly[condition.left.name] = (_inf, sup)
                return self
            elif condition.operator == BinaryComparisonOperation.Operator.LtE:
                assert isinstance(condition.left, VariableIdentifier)
                assert isinstance(condition.right, Literal)
                lower = -inf
                upper = eval(condition.right.val)
                self.bounds[condition.left.name].meet(IntervalLattice(lower, upper))
                bounds = self.bounds[condition.left.name]
                _inf: Dict[str, float] = dict()
                _inf['_'] = bounds.lower
                sup: Dict[str, float] = dict()
                sup['_'] = bounds.upper
                self.poly[condition.left.name] = (_inf, sup)
                return self
        # elif isinstance(condition, PyTcons1):
        #     abstract1 = self.domain(manager, self.environment, array=PyTcons1Array([condition]))
        #     self.state = self.state.meet(abstract1)
        #     return self
        elif isinstance(condition, set):
            assert len(condition) == 1
            self.assume(condition.pop(), bwd=bwd)
            return self
        raise NotImplementedError(f"Assumption of {condition.__class__.__name__} is unsupported!")

    @copy_docstring(State._substitute)
    def _substitute(self, left: Expression, right: Expression) -> 'ProductState':
        raise NotImplementedError(f"Call to _substitute is unexpected!")

    def affine(self, left: List[PyVar], right: List[PyTexpr1]) -> 'ProductState':
        if self.is_bottom():
            return self
        assignments = dict()
        for lhs, expr in zip(left, right):
            name = str(lhs)
            rhs = texpr_to_dict(expr)
            # update self.poly
            _inf, inf = deepcopy(rhs), deepcopy(rhs)
            _sup, sup = deepcopy(rhs), deepcopy(rhs)
            self.poly[name] = (_inf, _sup)
            #
            while any(variable in inf and variable not in self.inputs for variable in self.poly):
                for variable in self.poly:
                    if variable in inf and variable not in self.inputs:      # should be replaced
                        coeff = inf[variable]
                        if coeff > 0:
                            replacement = self.poly[variable][0]
                        elif coeff < 0:
                            replacement = self.poly[variable][1]
                        else:  # coeff == 0
                            replacement = dict()
                            replacement['_'] = 0.0
                        del inf[variable]
                        for var, val in replacement.items():
                            if var in inf:
                                inf[var] += coeff * val
                            else:
                                inf[var] = coeff * val
            while any(variable in sup and variable not in self.inputs for variable in self.poly):
                for variable in self.poly:
                    if variable in sup and variable not in self.inputs:      # should be replaced
                        coeff = sup[variable]
                        if coeff > 0:
                            replacement = self.poly[variable][1]
                        elif coeff < 0:
                            replacement = self.poly[variable][0]
                        else:  # coeff == 0
                            replacement = dict()
                            replacement['_'] = 0.0
                        del sup[variable]
                        for var, val in replacement.items():
                            if var in sup:
                                sup[var] += coeff * val
                            else:
                                sup[var] = coeff * val
            lower = evaluate(inf, self.bounds)
            upper = evaluate(sup, self.bounds)
            # update self.symbols
            for sym, val in self.symbols.values():
                rhs = substitute_in_dict(rhs, sym, val)
            assignments[name] = (name, rhs)
            bound = evaluate(rhs, self.bounds)
            # update bounds
            _lower = max(lower.lower, bound.lower)
            _upper = min(upper.upper, bound.upper)
            self.bounds[name] = IntervalLattice(_lower, _upper)
        self.symbols = assignments
        return self

    def relu(self, stmt: PyVar, active: bool = False, inactive: bool = False) -> 'ProductState':
        if self.is_bottom():
            return self
        self.flag = None

        name = str(stmt)
        lattice: IntervalLattice = self.bounds[name]
        lower, upper = lattice.lower, lattice.upper
        if upper <= 0 or inactive:
            zero = dict()
            zero['_'] = 0.0
            self.symbols[name] = (name, zero)

            # l_j = u_j = 0
            self.bounds[name] = IntervalLattice(0, 0)
            # 0 <= x_j <= 0
            zero: Dict[str, float] = dict()
            zero['_'] = 0.0
            self.poly[name] = (zero, zero)
            self.flag = -1
        elif 0 <= lower or active:
            if active and lower < 0:
                bounds = self.bounds[name]
                self.bounds[name] = bounds.meet(IntervalLattice(0, upper))
                sup = self.poly[name][1]
                zero: Dict[str, float] = dict()
                zero['_'] = 0.0
                self.poly[name] = (zero, sup)
            self.flag = 1
        else:
            _active, _inactive = deepcopy(self.bounds), deepcopy(self.bounds)
            _active[name] = _active[name].meet(IntervalLattice(0, upper))
            _inactive[name] = _inactive[name].meet(IntervalLattice(0, 0))

            if any(element.is_bottom() for element in _active.values()):
                zero = dict()
                zero['_'] = 0.0
                self.symbols[name] = (name, zero)
                self.flag = -1
            elif any(element.is_bottom() for element in _inactive.values()):
                self.flag = 1
            else:
                del self.symbols[name]
                self.flag = None

            join = dict()
            for variable, itv in _active.items():
                join[variable] = itv.join(_inactive[variable])
            if upper <= -lower:  # case (b) in Fig. 4, equation (3)
                # l_j = 0 && u_j = u_i
                self.bounds[name] = join[name].meet(IntervalLattice(0, upper))
                # 0 <= x_j <= u_i * (x_i - l_i) / (u_i - l_i)
                zero: Dict[str, float] = dict()
                zero['_'] = 0.0
                #
                m = upper / (upper - lower)
                if m > 0:
                    sup = self.poly[name][1]
                elif m < 0:
                    sup = self.poly[name][0]
                else:  # m == 0
                    sup = dict()
                    sup['_'] = 0.0
                for var, val in sup.items():
                    sup[var] = m * val
                q = - upper * lower / (upper - lower)
                sup['_'] = sup['_'] + q
                #
                self.poly[name] = (zero, sup)
                self.flag = None
            else:  # case (c) in Fig. 4, equation (4)

                # l_j = l_i && u_j = u_i
                self.bounds[name] = join[name].meet(IntervalLattice(lower, upper))
                    # join[name].meet(IntervalLattice(lower, upper))
                # print("after join and meet = {}".format(self.bounds[name].lower))
                # x_i <= x_j <= u_i * (x_i - l_i) / (u_i - l_i)
                inf = deepcopy(self.poly[name][0])
                #
                m = upper / (upper - lower)
                if m > 0:
                    sup = self.poly[name][1]
                elif m < 0:
                    sup = self.poly[name][0]
                else:  # m == 0
                    sup = dict()
                    sup['_'] = 0.0
                for var, val in sup.items():
                    sup[var] = m * val
                q = - upper * lower / (upper - lower)
                sup['_'] = sup['_'] + q
                #
                self.poly[name] = (inf, sup)
                # print("Case 4.c), lj = {}".format(self.bounds[name].lower))
                self.flag = None

        return self

    def outcome(self, outcomes: Set[VariableIdentifier]):
        found = None
        if self.is_bottom():
            found = '⊥'
        else:
            for chosen in outcomes:
                outcome = self.bounds[chosen.name]
                lower = outcome.lower
                unique = True
                remaining = outcomes - {chosen}
                for discarded in remaining:
                    alternative = self.bounds[discarded.name]
                    upper = alternative.upper
                    if lower <= upper:
                        unique = False
                        break
                if unique:
                    found = chosen
                    break
        return found
