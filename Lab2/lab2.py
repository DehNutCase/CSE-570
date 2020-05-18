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

def first(x, grammar, prev, this, first_time):
  #computes 'first,' the set of terminals that begin strings
  #derived from x
  #Hackish solution using first_time to allow recusively
  #adding to first
  #first_time has to be initialized to be larger than the number
  #on non_terminals
  #very inefficient solution
  first_x = {}
  first_time -= 1
  
  #if x is a terminal, x is the only thing in first(x)
  if (x in grammar['terminals'] or x == 'e'):
    first_x[x] = True
    return first_x
  #If we're here, x isn't a terminal
  else:
    if 'e' in grammar[x]:
      first_x['e'] = True
    for i in grammar[x]:
      broken = False
      prev = this
      this = first_x
      if this != prev or first_time:
        for j in i:
          first_j = first(j, grammar, prev, this, first_time)
          for k in first_j:
            #everything in first(j) is in first(x)
            if k != 'e':
              first_x[k] = True
            
          #if j can't turn into 'e' then nothing after join
          #can be in first(x), since j blocks it
          if not 'e' in first_j:
           broken = True
           break
          #if 'e' is in everything, then 'e' is in first_x
        if not broken:
          first_x['e'] = True

    return first_x

def first_string(string_x, grammar):
  #computes 'first,' the set of terminals that begin strings
  #derived from x, except x may be a string of grammar symbols
  #rather than a single symbol
  
  first_string_x = {}
  index = 0
  while (index < len(string_x)):
    first_index = first(string_x[index], grammar, {}, {}, 5)
    for i in first_index:
      if i != 'e':
        first_string_x[i] = True
        
    #stop looping if 'e' isn't part of first_index
    #if 'e' is part of everything, then 'e' is part of string_x
    first_string_x.pop('e', False)
    if not 'e' in first_index:
      break
    first_string_x['e'] = True
    index += 1
  
  return first_string_x

def follow(x, start, grammar, prev, this, first_time):
  #computes 'follow,' the set of terminals that can appear
  #immediately to the right of x in a sentential form
  
  #follow only accepts non-terminals for x
  if x in grammar['terminals']:
    return False
    
  follow_x = {}
  #'$' is our special endmarker symbol
  if x == start:
    follow_x['$'] = True
  
  #If there's a production A -> αBβ, then everything in first(β)
  #other than 'e,' is in follow(B)
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
          first_b = first_string(j[index+1], grammar)
          for k in first_b:
            if k != 'e':
              follow_x[k] = True
              
          #if 'e' is in first(β), everything in Follow(i) is in Follow(B)
          if 'e' in first_b:
            for k in follow(i, start, grammar, prev, this, False):
              follow_x[k] = True
        index += 1
        
      #we're now at the very last symbol, if it's B then everything in follow(A)
      #is in follow(B)
      #we need to stop doing this once follow sets stop being added to
      if j[index] == x:
        prev = this
        this = follow_x
        if this != prev or first_time:
          for k in follow(i, start, grammar, prev, this, False):
            follow_x[k] = True
        

  return follow_x
      
  
file = open('g417', 'r')
grammar, start = read_grammar_file(file)

print('For file = "g417":')
print('Printing firsts:')
for i in grammar:
  if i == 'terminals':
    continue
  print(i + ':')
  for j in first(i, grammar, {}, {}, 5):
    print(j, end = '')
  print('')

print('')
print('Printing follows:')
for i in grammar:
  if i == 'terminals':
    continue
  print(i + ':')
  for j in follow(i, start, grammar, {}, {}, True):
    print(j, end = '')
  print('')

file = open('g419', 'r')
grammar, start = read_grammar_file(file)

print('For file = "g419":')
print('Printing firsts:')
for i in grammar:
  if i == 'terminals':
    continue
  print(i + ':')
  for j in first(i, grammar, {}, {}, 5):
    print(j, end = '')
  print('')

print('')
print('Printing follows:')
for i in grammar:
  if i == 'terminals':
    continue
  print(i + ':')
  for j in follow(i, start, grammar, {}, {}, True):
    print(j, end = '')
  print('')

