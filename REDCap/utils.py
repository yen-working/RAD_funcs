import operator
import pandas as pd

def get_operator_function(operator_string: str):
    """Returns the function corresponding to the given operator string."""
    operator_string = operator_string.strip()

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '//': operator.floordiv,
        '%': operator.mod,
        '**': operator.pow,
        '=': operator.eq,
        '<>': operator.ne,
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le,
    }
    return operators.get(operator_string)

def check_equality(first_val, second_val):
    """For when comparing REDCap empty string with Pandas NaN."""
    print('first_value:', first_val)
    if first_val != "''" and first_val != '':
        return first_val == second_val
    
    if pd.isna(second_val):
        return True
    return False
