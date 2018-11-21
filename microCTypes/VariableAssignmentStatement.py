from microCTypes.Statement import Statement
from microCTypes.Variable import Variable
from microCTypes.ArithmeticExpression import ArithmeticExpression


class VariableAssignmentStatement(Statement):

    variable_name: str

    def __init__(self, variable, value):
        """

        :param variable_name:
        :param value: ArithmeticExpression
        """

        if type(variable) == Variable:
            if type(value) == int:
                super().__init__("{} = {}".format(variable.getName(), value), "Variable Assignment")
            else:
                super().__init__("{} = {}".format(variable.getName(), value.getExpression()), "Variable Assignment")
        else:
            if type(value) == int:
                super().__init__("{} = {}".format(variable, value), "Variable Assignment")
            else:
                super().__init__("{} = {}".format(variable, value.getExpression()), "Variable Assignment")


        # super().__init__(variable.getName() + value.getExpression(), "Variable")
        if not type(variable) == str:
            variable.value = value





