import operator
import pandas as pd

#--------------------------------------------------------
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

#--------------------------------------------------------
def check_equality(first_val, second_val):
    """For when comparing REDCap empty string with Pandas NaN."""
    print('first_value:', first_val)
    if first_val != "''" and first_val != '':
        return first_val == second_val
    
    if pd.isna(second_val):
        return True
    return False

#--------------------------------------------------------
def check_checkbox_redcap_var(redcap_variable: str):
    '''
    Check if `redcap_variable` is a checkbox variable.
    A checkbox variable would have two underscores before its final part.
    Example:

    checkbox_variable___1
    Two conditions:
    1. '___' is in redcap_variable
    2. '___' is the last underscore occurrence in redcap_variable
    '''
    if ('__' in redcap_variable) and (redcap_variable.rindex('_') == (redcap_variable.rindex('___') + 2)):
        return True
    return False


#--------------------------------------------------------
def extract_variable(redcap_variable: str):
    '''
    Extract the original variable if it is a multichoice variable.
    '''
    if check_checkbox_redcap_var(redcap_variable):
        # Case where the checkbox has a negative number option.
        try:
            end = redcap_variable.rindex('____')
        except ValueError:
            end = redcap_variable.rindex('___')
        before_choice = redcap_variable[:end]
        return before_choice
    return redcap_variable

def get_field_instru_map(instru_field_map: dict):
    '''
    Get lookup table for every variable in redcap project.
    '''
    field_instru_map = dict()
    for instru in instru_field_map:
        for field in instru_field_map[instru]:
            field_instru_map[field] = instru

    return field_instru_map