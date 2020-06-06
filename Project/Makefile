# general principles of make -
# lines are of the form

# target: ingredients
# (tab)	instruction to make target.

# sensitive to format - target definitions must begin in 
# first column, instruction lines must begin with tab
# lines beginning in # are comments

# when you type "make", the first target listed in the file
# is built (you can get any target by typing "make thing" -
# for example to make just pre.o here I would type
# "make pre.o"

# if the target is missing or is older than any of the ingredients,
# then it is made - else nothing happens.

# same rules apply when making any of the ingredients.
# some targets may be completely independent of the ultimate
# result (like clean and print, below)

# these are definitions that fill in $FLAGS and $CC below
# -ggdb inserts hooks for debugger into compiled code
# gcc is the gnu C compiler

FLAGS := -ggdb
CC := gcc

# the final executable result - spf (subset PFortran compiler)
# (a parallel extension to Fortran)

# spf is built from the 4 specified object files
# the line below the spf definition is the instruction
# to the gcc compiler to build the executable 

spf: pre.o cal.o lex.o hash.o
	$(CC) $(FLAGS) pre.o hash.o cal.o lex.o -o spf

# the following 4 lines are how to build the ingredients for the 
# first line - the object files pre, gram, lex and hash


# hash table routines - used to build symbol table

hash.o: hash.c
	$(CC) $(FLAGS) -c hash.c -o hash.o

# preprocessor - massage fortran code so it is easier to write a
# grammar that handles it

pre.o: pre.c hash.h
	$(CC) $(FLAGS) -c pre.c -o pre.o

# the parser and code generator
# built from the C program and header that is output by yacc

cal.o: cal.tab.c hash.h
	$(CC) $(FLAGS) -c cal.tab.c -o cal.o

# the lex object file 
# built from the C program that is output by lex

lex.o: lex.yy.c
	$(CC) $(FLAGS) -c lex.yy.c -o lex.o

# the following lines build the c programs and header files
# needed to make the lexer and parser object files
# both the lexer and the parser need the symbol table, definitions
# for which are in hash.h

# builds the lexer program code from the lexical definition
# gram.l, and the header files created by yacc
#
# flex is gnu lex
# lex.yy.c is the default output name
lex.yy.c: cal.l cal.h cal.tab.h
	flex cal.l 

# builds the parser program code gram.tab.c from
# the grammar definition gram.y
#	
# bison is the gnu version of yacc
gram.tab.c: cal.y hash.h 
	bison --debug --verbose -d -k gram.y


# substitute the name of your .y file for "gram"
#
# the flags --debug --verbose cause bison to generate a listing
# called gram.output that describes the states, parse tables and
# specifies conflicts in the parser
# the flags -d -k generate gram.h, gram.tab.h which are header files
# used by lex.


# this is an instruction used to print all the relevant files
# called by typing "make printout"

printout: 
	enscript spf.h cal.h cal.tab.h hash.h pre.c hash.c cal.y cal.l makefile

# this instruction cleans up the temporary files left by the
# compilation process - this is also useful to force recompilation
# of everything (type "make clean" to invoke this.

clean:
	rm -f cal.tab.c lex.yy.c *.o *.spf spf.f core output