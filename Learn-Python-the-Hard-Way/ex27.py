import random

truth_table = { 'not False': 'True', 'not True': 'False', 'True or False': 'True', 'True or True': 'True', 'False or True': 'True', 'False or False': 'False', 'True and False': 'False', 'True and True': 'True', 'False and True': 'False', 'False and False': 'False', 'not (True or False)': 'False', 'not (True or True)': 'False', 'not (False or True)': 'False', 'not (False or False)': 'True', 'not (True and False)': 'True', 'not (True and True)': 'False', 'not (False and True)': 'True', 'not (False and False)': 'True', '1 != 0': 'True', '1 != 1': 'False', '0 != 1': 'True', '0 != 0': 'False', '1 == 0': 'False', '1 == 1': 'True', '0 == 1': 'False', '0 == 0': 'True' }

print '\nAnswer True or False, type quit to exit.\n'

while True:
  key = random.choice(truth_table.keys())
  answer = raw_input('%s: ' % key)
  if answer == 'quit':
    break
  if answer == truth_table[key]:
    print 'Correct\n'
  else:
    print 'Wrong\n'

