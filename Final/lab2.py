# -*- coding: utf-8 -*-

def read_grammar_file(file):
  #takes a file of the format specified in http://www.cse.csusb.edu/egomez/cs570/lab4.txt
  #returns a dictionary of dictionaries
  #each dictionary inside the root dictionary is a non-terminal
  #each entry inside a non-terminal is a production
  #the dictionary named 'terminals' is an exception
  #it's a dictionary of terminals
  #Also returns the start symbol as a string
  
  grammar = {'terminals':{}}
  next = file.readline().strip()
  start = False
  #read all the terminals and add them to the 'terminals' dictionary
  while (next != '$'):
    grammar['terminals'][next] = True
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
      
  
file = open('f1', 'r')
grammar, start = read_grammar_file(file)
first_g417 = {}

print('For file = "f1":')
print('Printing Productions:')
for i in sorted(grammar):
  if i == 'terminals':
    continue
  print(i + ':')
  for j in sorted(grammar[i]):
    print(j)
  print('')

print('Printing firsts:')
for i in sorted(grammar):
  if i == 'terminals':
    continue
  print(i + ':')
  for j in sorted(first_x(i, grammar, {}, {})):
    print(j, end = "")
  print('')
  
print('')
print('Printing follows:')
for i in sorted(grammar):
  if i == 'terminals':
    continue
  print(i + ':')
  for j in sorted(follow(i, start, grammar, {}, {})):
    print(j, end = '')
  print('')

print('')
print('')
