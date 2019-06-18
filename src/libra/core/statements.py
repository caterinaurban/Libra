"""
Statements
==========

Libra's internal representation of Python statements.

:Authors: Caterina Urban
"""

from abc import ABCMeta, abstractmethod
from typing import List, Set

from libra.core.expressions import Expression, VariableIdentifier


class ProgramPoint:
    def __init__(self, line: int, column: int):
        """Program point representation.

        :param line: line of the program
        :param column: column of the program
        """
        self._line = line
        self._column = column

    @property
    def line(self):
        return self._line

    @property
    def column(self):
        return self._column

    def __eq__(self, other: 'ProgramPoint'):
        return (self.line, self.column) == (other.line, other.column)

    def __hash__(self):
        return hash((self.line, self.column))

    def __ne__(self, other: 'ProgramPoint'):
        return not (self == other)

    def __repr__(self):
        """Unambiguous string representation of the program point

        :return: unambiguous string representation
        """
        return "[line:{0.line}, column:{0.column}]".format(self)


class Statement(metaclass=ABCMeta):
    """Statement representation.

    https://docs.python.org/3.4/reference/simple_stmts.html
    """

    def __init__(self, pp: ProgramPoint):
        """Statement construction.

        :param pp: program point associated with the statement
        """
        self._pp = pp

    @property
    def pp(self):
        return self._pp

    @abstractmethod
    def __repr__(self):
        """Unambiguous string representation of the statement.

        :return: string representing the statement
        """

    def ids(self) -> Set[VariableIdentifier]:
        """Identifiers that appear in the statement.

        :return: set of identifiers that appear in the statement
        """
        ids = set()
        for stmt in _walk(self):
            if isinstance(stmt, VariableAccess):
                ids.add(stmt.variable)
        return ids


def _iter_child_exprs(stmt: Statement):
    """
    Yield all direct child expressions of ``stmt``,
    that is, all fields that are statements
    and all items of fields that are lists of statements.
    """
    for _, field in stmt.__dict__.items():
        if isinstance(field, Statement):
            yield field
        elif isinstance(field, list):
            for item in field:
                if isinstance(item, Statement):
                    yield item


def _walk(stmt: Statement):
    """
    Recursively yield all statements in an statement tree
    starting at ``stmt`` (including ``stmt`` itself),
    in no specified order.
    """
    from collections import deque
    todo = deque([stmt])
    while todo:
        stmt = todo.popleft()
        todo.extend(_iter_child_exprs(stmt))
        yield stmt


"""
Expression Statements.
https://docs.python.org/3.4/reference/simple_stmts.html#expression-statements
"""


class LiteralEvaluation(Statement):
    """Literal evaluation representation."""

    def __init__(self, pp: ProgramPoint, literal: Expression):
        """Literal evaluation construction.

        :param pp: program point associated with the literal evaluation
        :param literal: literal being evaluated
        """
        super().__init__(pp)
        self._literal = literal

    @property
    def literal(self):
        return self._literal

    def __repr__(self):
        return "{0.literal}".format(self)


class VariableAccess(Statement):
    """Variable access representation."""

    def __init__(self, pp: ProgramPoint, variable: VariableIdentifier):
        """Variable access construction.

        :param pp: program point associated with the variable access
        :param variable: variable being accessed
        """
        super().__init__(pp)
        self._variable = variable

    @property
    def variable(self):
        return self._variable

    def __repr__(self):
        return "{0.variable}".format(self)


"""
Assignment Statements.
https://docs.python.org/3.4/reference/simple_stmts.html#assignment-statements
"""


class Assignment(Statement):
    """Assignment Statements.

    https://docs.python.org/3.4/reference/simple_stmts.html#assignment-statements
    """

    def __init__(self, pp: ProgramPoint, left: VariableAccess, right: Statement):
        """Assignment statement representation.

        :param pp: program point associated with the statement
        :param left: left-hand side of the assignment
        :param right: right-hand side of the assignment
        """
        super().__init__(pp)
        self._left = left
        self._right = right

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def __repr__(self):
        return "{0.left} = {0.right}".format(self)


"""
Call Statements.
"""


class Call(Statement):
    def __init__(self, pp: ProgramPoint, name: str, arguments: List[Statement]):
        """Call statement representation.

        :param pp: program point associated with the call
        :param name: name of the function/method being called
        :param arguments: list of arguments of the call
        """
        super().__init__(pp)
        self._name = name
        self._arguments = arguments
        self._activated = True

    @property
    def name(self):
        return self._name

    @property
    def arguments(self):
        return self._arguments

    @property
    def activated(self):
        return self._activated

    @activated.setter
    def activated(self, activation):
        self.activated = activation

    def __repr__(self):
        arguments = ", ".join("{}".format(argument) for argument in self.arguments)
        return "{}({})".format(self.name, arguments)
