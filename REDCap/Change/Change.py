"""
A class that stores a field's name, its old value and its new value.
"""


################################################################################
class Change:
    # --------------------------------------------------------------------------
    def __init__(self, field_name: str, old_value, new_value):
        """
        Initialize the Change class.

        Inputs:
        --------
        field_name: str
            REDCap field_name.
        old_value:
            Field's old value.
        new_value:
            Field's new value.
        """
        self.field_name = field_name
        self.old_value = old_value
        self.new_value = new_value
