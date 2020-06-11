# -*- coding: utf-8 -*-
import json
#we need this to convert dicts to strings and back
import copy
#dictionaries are mutable, so we want to deep copy them to make copies
#rather than modifying what's already there

def read_grammar_file(file):
  #takes a file of the format specified in http://www.cse.csusb.edu/egomez/cs570/lab4.txt
  #returns a dictionary of dictionaries
  #each dictionary inside the root dictionary is a non-terminal
  #each entry inside a non-terminal is a production
  #the dictionary named "terminals" is an exception
  #it's a dictionary of terminals
  #Also returns the start symbol as a string
  
  grammar = {"terminals":{}}
  next = file.readline().strip()
  start = False
  #read all the terminals and add them to the "terminals" dictionary
  while (next != '$'):
    grammar["terminals"][next] = True
    next = file.readline().strip()
    
  next = file.readline().strip()
  #we're assuming the first entry is the start variable
  
  #read all the productions and add them to the dictionary
  while (next != '$'):
    line = next.split('->')
    next = file.readline().strip()
    non_terminal = line[0]
    production = line[1]
    if (not start):
      start = non_terminal
    
    if non_terminal in grammar:
      grammar[non_terminal][production] = True
    else:
      grammar[non_terminal] = {}
      grammar[non_terminal][production] = True
      
  file.close()
  return grammar, start

def closure(item, grammar):
  #An item is a dictionary of the form item = {A: {α.Bβ:True}}
  #Each entry corresponds to a non-terminal, which is represented as a dictionary
  #containing productions of the form α.Bβ, which represents A → α.Bβ
  #The '.' marks where we've processed up to
  #Closure takes an item and a grammar and returns the closure, a state
  #which contains everything in the item and every production derivable without
  #moving the period (processing input)
  #the closure item is a state, and will need to be given a name
  #however, items should be defined by their kernels, which are states
  #A kernel of an item is the initial item and all items where the period
  #is not the first item
  #A kernel is of the form {"S":".S", "Y":"a.Sb"} (same as every other item)
  
  closure_item = copy.deepcopy(item) #step 1, add everything in I to closure
  prev = {}
  
  #step 2
  while (closure_item != prev):
    #keep repeating step 2 until no more items are added
    prev = copy.deepcopy(closure_item) #this checks for added items
    future = copy.deepcopy(closure_item)
    
    #for each item in closure(i) of the form A → α.Bβ
    #If there are one or more items in grammar of the form B -> γ
    #add B -> .γ to closure(i)
    for non_terminal in closure_item:
      for production in closure_item[non_terminal]:
        index = 0
        while (index < len(production) - 1):
          #search for "." before the last character
          #nothing to add if "." is last
          if production[index] != ".":
            index += 1
            continue
          
          B = production[index + 1]
          #if we're here we found "."
          if B in grammar["terminals"] or B == 'e':
            break #nothing to add if B isn't a non_terminal
          
          #if we're here B is a non_terminal
          if not B in future:
            future[B] = {} #Add B to closure_item
          
          for i in grammar[B]:
            #every i is a production of B
            future[B]["." + i] = True #add B -> .i to closure_item
          break
    closure_item = future

  return closure_item

def goto(item, symbol, grammar):
  #Given an item, a grammar symbol (terminal or non_terminal), and a grammar
  #computes the kernel of a state produced by moving the period
  #the productions of the item over the symbol, going from
  #A -> a.Xb to A -> aX.b, and using these new productions are the kernel
  #for a (possibly) new state

  goto_kernel = {}
  
  for non_terminal in item:
    #go over each production of the form non_terminal -> key of item[non_terminal]
    #item[non_terminal] is a dictionary where the keys are productions
    for production in item[non_terminal]:
      #For each non_terminal -> production
      #search for "."
      index = 0
      while (index < len(production) - 1):
        #search for "." before the last character
        #nothing to add if "." is last
        if production[index] != ".":
          index += 1
          continue
        
        if production[index + 1] != symbol:
          break #only move the period over the symbol given
          
        #if we're here we found something to add
        
        if not non_terminal in goto_kernel:
          goto_kernel[non_terminal] = {} #add non_terminal to kernel
        
        new_production = production[:index] + symbol + "." + production[index +2:]
        #new_production goes from "A.XB" to "AX.B"
        goto_kernel[non_terminal][new_production] = True
        break #we added to kernel, no more need to search
  
  return goto_kernel
  
def canonical(grammar, start):
  #constructs the canonical states of a grammar
  #note that the states only contain their kernels, you need to call
  #closure to get the full state
  #canonical returns a dictionary that uses the kernels of states as keys
  #and state id as values
  #additionally, each state is in the form [state, symbol]
  #and the symbol is the symbol used in goto to reach that state
  #call closure on states to obtain the full state
  
  #initial = closure({"S'": {"." + start: True}}, grammar)
  initial = {"S'": {"." + start: True}}
  states = {json.dumps([initial, "S'"]): True}
  #states contains keys of the form json.dumps([item, symbol])
  #to retrieve the item we need to call json.loads(key), and take the 0th index
  #The initial state should have the modified start symbol S' associated with it
  
  
  prev = {}
  state_index = 0
  while prev != states:
    #repeat until no changes
    prev = copy.deepcopy(states)
    future = copy.deepcopy(states)
    
    for key in states:
      #each key in states is a json.dumps([item, symbol])
      #we need to retrieve item and call 
      if type(states[key]) != bool:
        #we already processed this, look at the next key
        #if we haven't processed a key it should still be a boolean
        continue
      
      item = closure(json.loads(key)[0], grammar)
      #each item is a dictionary with non_terminals as keys, where each value
      #is a dictionary containing productions as keys
      #we take the closure because the dictionary only contains kernels
      
      symbols = {} #we need to find the symbols with a dot on the left
      #being a dictionary makes it trivial to check if a symbol in in symbols
      for non_terminal in item:
        for production in item[non_terminal]:
          index = 0
          while (index < len(production) - 1):
          #search for "." before the last character
          #nothing to add if "." is last
            if production[index] != ".":
              index += 1
              continue
            
            #if we're here we found something to add
            symbols[production[index+1]] = True #add the symbol as a key to symbols
            break #found the symbol after the period, so we can break
      
      #calculate goto(I, X) for all X == symbol
      #States will only contain kernels at the end, make sure to call closure
      #if the full state is needed      
      for symbol in symbols:
        goto_symbol = goto(item, symbol, grammar)
        if goto_symbol: #if goto_symbol isn't empty
          goto_json = json.dumps([goto_symbol, symbol])
          if not goto_json in states: #and goto_symbol isn't in states
            future[goto_json] = True #add it to states
      
      #we mark a state as processed by giving it an index number
      #if a state has a state_index of 1 it's item I1
      future[key] = state_index
      state_index += 1
    
    states = future
    
  return states
  
file = open('f1', 'r')
grammar, start = read_grammar_file(file)

print('For file = "f1":')
print('Printing Productions:')
for i in sorted(grammar):
  if i == 'terminals':
    continue
  print(i + ':')
  for j in sorted(grammar[i]):
    print(j)
  print('')

print("Printing kernels of the canonical states of the grammar:")
temp = canonical(grammar,start)
#canonical returns a dictionary that uses the kernels of states as keys
#and state id as values
#additionally, each state is in the form [json.dumps(state), symbol]
#and the symbol is the symbol used in goto to reach that state
#call closure on states to obtain the full state
#because state is in json form, we need to call json.loads(state)
print("")
to_print = []

for i in temp:
  to_print.append([i, temp[i]])

def second_entry(a_list):
  return a_list[1]
to_print.sort(key=second_entry)

print("Format of a state is: [{dictionary of non_terminals: dictionary of productions}, symbol]")
print("i.e. a state of the form [{'S': {'.A': true}}, '('] has the production S -> .A, and is reached")
print("by calling goto(I, '(')")
print("")

for i in to_print:
  #each i is a state
  #the first item in each i is a dictionary with keys being non_terminals
  #and values being dictionaries containing productions as keys
  #the second item in i is the numeric state id of the state
  print("State #", i[1], " is")
  print(i[0])
  
print("")

print("Printing the canonical states of the grammar:")
print("Obtained by calling closure(I) on the kernel of a state")

for i in to_print:
  print("State #", i[1], " is")
  state_list = json.loads(i[0]) #unpacking the state dictionary from JSON
  print("Obtained by goto(I, ", state_list[1], ")")
  print(closure(state_list[0], grammar))

print("")