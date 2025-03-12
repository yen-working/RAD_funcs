'''
A class that stores a filter and the changes that follow that condition (if any).
'''

from Change.Change import Change
from utils import get_operator_function


################################################################################
class Filter:
    # --------------------------------------------------------------------------
    def __init__(self, condition: str, changes: list[Change] = []):
        """
        Initialize the ConditionChanges class.

        Inputs:
        --------
        condition: str
            REDCap filter logic.
        changes: list[Change]
            List of changes.
        """
        self.condition = condition
        self.condition_obj = self.get_condition_obj()
        self.condition_field = self.condition_obj['field_name']
        self.condition_operator = self.condition_obj['operator']
        self.condition_value = self.condition_obj['value']
        self.changes = changes


    def get_condition_obj(self):
        '''
        Translate REDCap filter logic string into object.
        Right now this only works for logic that has one field name in it.
        TODO: include handling of multiple field names
        '''
        condition = self.condition
        condition_obj = dict()

        open_bracket_index = condition.index('[')
        close_bracket_index = condition.index(']')
        # Extract field name
        field_name = condition[(open_bracket_index+1):close_bracket_index]
        condition_obj['field_name'] = field_name

        first_space_index = condition.index(' ')
        second_space_index = condition[(first_space_index + 1):].index(' ') + (first_space_index + 1)

        # Extract operator
        op = condition[(first_space_index + 1):second_space_index]
        op = get_operator_function(op)
        
        condition_obj['operator'] = op

        # Extract value
        value = condition[(second_space_index+1):]
        condition_obj['value'] = value

        return condition_obj






