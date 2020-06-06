# A Makefile for simple lex and yacc examples

# Comment out the proper lines below according to the scanner and
# parser generators available in your system

LEX = lex
YACC = yacc -d
# LEX = flex 
# YACC = bison -d

# We assume that your C-compiler is called cc

CC = cc

# cal is the final object that we will generate, it is produced by
# the C compiler from the y.tab.o and from the lex.yy.o

cal: y.tab.o lex.yy.o
	$(CC) -o cal y.tab.o lex.yy.o -ll -lm 

# These dependency rules indicate that (1) lex.yy.o depends on
# lex.yy.c and y.tab.h and (2) lex.yy.o and y.tab.o depend on cal.h.
# Make uses the dependencies to figure out what rules must be run when
# a file has changed.

lex.yy.o: lex.yy.c y.tab.h
lex.yy.o y.tab.o: cal.h

## This rule will use yacc to generate the files y.tab.c and y.tab.h
## from our file cal.y

y.tab.c y.tab.h: cal.y
	$(YACC) -v cal.y

## this is the make rule to use lex to generate the file lex.yy.c from
## our file cal.l

lex.yy.c: cal.l
	$(LEX) cal.l

## Make clean will delete all of the generated files so we can start
## from scratch

clean:
	-rm -f *.o lex.yy.c *.tab.*  cal *.output
