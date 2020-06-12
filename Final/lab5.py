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

def first_x(x, grammar, first, first_prev):
  #computes 'first,' the set of terminals that begin strings
  #derived from x
  #x is a single character, not a string
  if not x in first:
    first[x] = {}
  
  #if x is a terminal, x is the only thing in first(x)
  if (x in grammar['terminals'] or x == 'e'):
    first[x][x] = True
    return first[x]
    
  #If we're here, x isn't a terminal
  if 'e' in grammar[x]:
    first[x]['e'] = True
  
  #we need to repeat this step until none of the first sets in
  #the grammar changes
  while first != first_prev:
    first_prev = first.copy() #this will check for changes
    #dictionaries are mutable types, so first_prev = first would make 
    #the two dictionaries point to the same thing
    #make sure to use .copy()
    
    for i in grammar[x]:
      #each i is a production, a production is in the form Y1Y2Y3...
      index = 0
      while (index < len(i)):
        first_index = first_x(i[index], grammar, first, first_prev)
        
        for j in first_index:
          first[i[index]][j] = True
        for j in first[i[index]]:
          if j != 'e':
            first[x][j] = True
        
        if not 'e' in first[i[index]]:
          break
        index += 1
        if (index >= len(i)):
          first[x]['e'] = True

  return first[x]

def first_string(string_x, grammar, first, first_prev):
  #computes 'first,' the set of terminals that begin strings
  #derived from x, except x may be a string of grammar symbols
  #rather than a single symbol
  
  first_string_x = {}
  index = 0
  while (index < len(string_x)):
    first_index = first_x(string_x[index], grammar, first, first_prev) #not sure if this works properly
    for i in first_index:
      if i != 'e':
        first_string_x[i] = True
        
    #stop looping if 'e' isn't part of first_index
    #if 'e' is part of everything, then 'e' is part of string_x
    if not 'e' in first_index:
      break
    index += 1
    if index >= len(string_x):
      first_string_x['e'] = True
  
  return first_string_x

def follow(x, start, grammar, follow_this, follow_prev):
  #computes 'follow,' the set of terminals that can appear
  #immediately to the right of x in a sentential form
  
  #follow only accepts non-terminals for x
  if x in grammar['terminals']:
    return False
    
  if not x in follow_this:
    follow_this[x] = {}
    
  #'$' is our special endmarker symbol
  if x == start:
    follow_this[x]['$'] = True
  
  #If there's a production A -> αBβ, then everything in first(β)
  #other than 'e,' is in follow(B)
  
  while follow_this != follow_prev:
    follow_prev = follow_this.copy()
    
    for i in grammar:
      #our grammar contains terminals and non-terminals
      #we're ignoring terminals since they dont' have productions
      if i == 'terminals':
        continue
      
      for j in grammar[i]:
        #search through every production for something of the form αBβ
        #α is allowed to be 'e'
        index = 0
        while (index < len(j) - 1):
          if j[index] == x:
            #αBβ, everythign in first(β) is in follow(B)
            first_b = first_string(j[index+1:], grammar, {}, {})
            for k in first_b:
              if k != 'e':
                follow_this[x][k] = True
                
            #if 'e' is in first(β), everything in Follow(i) is in Follow(B)
            if 'e' in first_b:
              if not i in follow_this:
                follow_this[i] = {}
              for k in follow(i, start, grammar, follow_this, follow_prev):
                follow_this[i][k] = True
              for k in follow_this[i]:
                follow_this[x][k] = True
          index += 1
          
        #we're now at the very last symbol, if it's B then everything in follow(A)
        #is in follow(B)
        if j[index] == x:
          if not i in follow_this:
            follow_this[i] = {}
          for k in follow(i, start, grammar, follow_this, follow_prev):
            follow_this[i][k] = True
          for k in follow_this[i]:
            follow_this[x][k] = True
        

  return follow_this[x]

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

def second_entry(a_list):
  #helper function to sort by second entry in a list
  return a_list[1]

def SLR_table(grammar, start):
  #constructs the SLR table for a grammar
  #table will be in the form of a dictionary with state_ids as keys
  #each value would be a dictionary with symbols as keys and the actions
  #as values

  #construct canonical states (their kernels, remember to use closure to unpack)
  C = canonical(grammar, start)
  to_sort = []
  for i in C:
    #using json.loads(i) we unpack each state into [state, symbol]
    #state is a dictionary with non_terminals as keys
    #the values are dictionaries of productions where productions are keys
    #the symbol is the symbol in goto(I, symbol)
    to_sort.append([json.loads(i), C[i]]) 
    
  to_sort.sort(key=second_entry)
  #states are now sorted by their state id
  for i in to_sort:
    i[0] = [closure(i[0][0], grammar), i[0][1]]
  #states are unpacked with closure
  #each state now has more information to deal with
  #but it makes processing easier (costs memory, but that isn't an issue)
  C = to_sort
  #C is now a list of states of the form
  #C[i] = [[item, symbol] ,state_id]
  
  parsing_table = {}
  #parsing table will be a dictionary of dictionaries
  #the keys to parsing_table will be state_ids
  #the values will be dictionaries where keys are symbols
  #and values are lists of actions
  #a list with multiple actions means there's a conflict
  
  for i in C:
    #each i is of the form [[item, symbol] ,state_id]
    #a state is defined by its item
    #the state_id is its id (arbitrary)
    #and the symbol is the synbol used to reach the state from another state
    
    #create an entry for the state
    parsing_table[i[1]] = {}
    
    item = i[0][0]
    for non_terminal in item:
      #go over each production of the form non_terminal -> key of item[non_terminal]
      #item[non_terminal] is a dictionary where the keys are productions
      for production in item[non_terminal]:
        #if [A -> α.aβ] is in a state, i, and goto(i, a) = state j, then 
        #action(i,a) is shift j. a is a terminal
        
        #For each non_terminal -> production
        #search for "."
        index = 0
        while (index < len(production) - 1):
          #search for "." before the last character
          #nothing to add if "." is last
          if production[index] != ".":
            index += 1
            continue
          
          #if we're there's a symbol after "." but before the end of the production
          index += 1
          symbol = production[index]
          
          if not (symbol in grammar['terminals'] or symbol == 'e'):
            break #break since below code is for terminals
          
          #we now need to find the state in C which matches [closure(goto(item, symbol, grammar), grammar), symbol]
          #so we can get its state_id
          
          state_to_match = [closure(goto(item, symbol, grammar), grammar), symbol]
          
          #if we don't have an entry for symbol in the parsing table, add it
          if not symbol in parsing_table[i[1]]:
            parsing_table[i[1]][symbol] = []
            
          #iterate through C to find the state we need to match
          for j in C:
            if j[0] == state_to_match:
              #we found the state
              #the action for i[1][symbol] should be shift j
              parsing_table[i[1]][symbol].append(["shift", j[1]])
          break
        
        #if [A -> α.] is in a state, i, then action(i, a) is
        #reduce A -> α for all α in Follow(A).
        #However, A must not be the symbol added to the augmented grammar
        #(That is, A != start + "'")
        
        #If [S' -> S.] is in I, then set action[i, S'] to "accept"
        #S is the start symbol, S' is the modified start symbol
        
        if production[-1] == ".":
          #A -> α. is a production if the last character in the production is "."
          symbol_string = production[:-1] #the symbol string we're parsing doesn't have "."
          #symbol string is now α
          
          if non_terminal == start + "'":
            #start + "'" is S'
            if symbol_string == start:
              #set action[i, S'] to "accept"
              #Alternatively, set action [i, $] to accept, we're using the alternative
              
              #symbol = start + "'"
              symbol = "$"
              
              #if we don't have an entry for symbol in the parsing table, add it
              if not symbol in parsing_table[i[1]]:
                parsing_table[i[1]][symbol] = []
              parsing_table[i[1]][symbol].append(["accept"])
              
          else:
            #non_terminal isn't S', so action(i, a) is reduce A -> α
            #for all a in Follow(A)
            symbols = follow(non_terminal, start, grammar, {}, {})
            
            for symbol in symbols:
              if not symbol in parsing_table[i[1]]:
                parsing_table[i[1]][symbol] = []
              parsing_table[i[1]][symbol].append(["reduce", non_terminal + "->" +symbol_string])
            
    for symbol in grammar:
      #the goto transitions for state i are constructed for all nonterminals A
      if symbol == "terminals":
        continue #terminals are not nonterminals
      
      #The rule is: if GOTO(i, A) = Ij, then goto(i, A) = j
      if not symbol in parsing_table[i[1]]:
        parsing_table[i[1]][symbol] = []
      
      state_to_match = [closure(goto(item, symbol, grammar), grammar), symbol]
      
      #iterate through C to find the state we need to match
      for j in C:
        if j[0] == state_to_match:
          #we found the state
          #the action for i[1][symbol] should be shift j
          parsing_table[i[1]][symbol].append(["goto", j[1]])
          
  print("")
  
  return parsing_table, C


  
  
file = open('f1', 'r')
grammar, start = read_grammar_file(file)

print('For file = "g5":')
parsing_table, states = SLR_table(grammar, start)
print("Printing states:")
print("Each state is of the form [[item, symbol] ,state_id]")
for i in states:
  print(i)

print("")

print("Printing parsing table:")
for i in parsing_table:
  print("State ", i, " ", parsing_table[i])


