"""A class representing a metric by specifying whether it's a sum, unique count, or average of an existing-metric.
Currently implemented actions:
- Sum
- Distinct count
- Ratio

Currently implemented fields:
- `patients`
- `studies`
"""

from typing import Literal

################################################################################
actions = Literal['SUM', 'DISTINCT', 'RATIO']
fields = Literal['patients', 'studies']
field_to_table = {
   'patients': ('patients', 'patient_name'),
   'studies': ('studies', 'study_uid')
}

class Metric:
   # --------------------------------------------------------------------------
   def __init__(self, action: actions, first_field: fields, second_field: fields = ''):
      self.action = self.validate_metric(action, first_field, second_field)
      self.first_field = first_field
      self.second_field = second_field
      self.sql = self.get_sql()

   # --------------------------------------------------------------------------
   def validate_metric(self, action, first_field, second_field):
      if first_field == '':
         raise ValueError('Field cannot be empty.')
      if action == 'RATIO' and second_field == '':
         raise ValueError('Second value cannot be empty when the action is RATIO.')
      if action != 'RATIO' and second_field != '':
         raise ValueError(f'Second field cannot be non-empty if the action is {action}.')
      return action   
    
   # --------------------------------------------------------------------------
   def get_sql(self):
      action = self.action
      first_field = self.first_field
      first_field_table = field_to_table[first_field][0]
      first_field_column = field_to_table[first_field][1]

      second_field = self.second_field

      if action == 'DISTINCT':
         return f'SELECT COUNT(DISTINCT {first_field_column}) FROM {first_field_table}'
      
      if action == 'RATIO':
         second_field_table = field_to_table[second_field][0]
         second_field_column = field_to_table[second_field][1]
         return f'''SELECT 
         (SELECT COUNT(DISTINCT {first_field_column}) FROM {first_field_table})
         (SELECT COUNT(DISTINCT {second_field_column}) FROM {second_field_table})'''

    
