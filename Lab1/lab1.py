def finite_automaton(input, transition_table, accepting_states):
  #input is a string of characters
  #transition_table is a dictionary of states containing a dictionary of transitions
  #starting state will always be assumed to be 0
  #accepting_states is a list of accepting states
  #returns true if input results in accepting state, otherwise false
  #this will always take O(n) time to complete, even if non-acceptance can be
  #determined earlier
  current_state = 0
  i = 0
  while (i < len(input)):
    current_state = transition_table[current_state][input[i]]
    i += 1
  if (current_state in accepting_states):
    return True
  else:
    return False

test_inputs = ['abbbbbbabb', 'abb', 'abbbbbba', 'abbbbb', 'bbbbabb']

#table for L=(a|b)*abb
test_table = {0:{'a':1, 'b':0}, 1:{'a':1, 'b':2}, 2:{'a':1, 'b':3}, 3:{'a':1, 'b':0}}

test_accept = [3]

print('test inputs are:', test_inputs)
for i in range(len(test_inputs)):
  print(finite_automaton(test_inputs[i], test_table, test_accept))