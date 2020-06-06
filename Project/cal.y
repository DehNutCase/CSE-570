%{
#include <stdio.h>
int regs[26];
int base;
int yylex();
int yyerror(char *s);
int yywrap();
int last = 0;
%}

%start list
%union {
  int a;
  char c;
}
%type <a> expr number DIGIT
%type <c> LETTER
%token DIGIT LETTER
%left '|'
%left '&'
%left '+' '-'
%left '*' '/' '%'
%left UMINUS

%%

list: /* empty */
    | list stat '\n'
    | list error '\n' {
      yyerrok;
    };

stat: expr {
        printf("%d\n", $1);
        last = $1; /* We memorize the last result.*/
      }
    | LETTER '=' expr {
      /* KL, this is what stores a value to a variable 
      Note that variables are single characters, lowercase
      due to their definition in cal.l 
      
      That is, this is the form of the assignment statement.
      */
      regs[$1] = $3;
    };
    | LETTER '='{
      /* KL, We allow storing variables from the last result.
      Typing LETTER = will cause LETTER to have the value of
      the last result.
      
      Note that last is initiated to 0 to prevent errors.
      */
      regs[$1] = $3;
    };
    | '*' expr {
        /* This is what uses the last result to calculate
        the next.
        
        That is, this is the form of the exit/quit feature
        (Since it doesn't start with an expr, we assume
        the first expr is simply the last value)
        */
        last = last * $2;
        printf("%d\n", last);
      }
    | '/' expr {
        last = last / $2;
        printf("%d\n", last);
      }
    | '%' expr {
        last = last % $2;
        printf("%d\n", last);
      }
    | '+' expr {
        last = last + $2;
        printf("%d\n", last);
      }
    | '-' expr {
        last = last - $2;
        printf("%d\n", last);
      }

expr: '(' expr ')' {
        $$ = $2;
      }
    | expr '*' expr {
        $$ = $1 * $3;
      }
    | expr '/' expr {
        $$ = $1 / $3;
      }
    | expr '%' expr {
        $$ = $1 % $3;
      }
    | expr '+' expr {
        $$ = $1 + $3;
      }
    | expr '-' expr {
        $$ = $1 - $3;
      }
    | expr '&' expr {
        $$ = $1 & $3;
      }
    | expr '|' expr {
        $$ = $1 | $3;
      }
    | '-' expr %prec UMINUS {
        $$ = -$2;
      }
    | LETTER {
        $$ = regs[$1];
      }
    | number;

number: DIGIT {
          $$ = $1;
          base = ($1 == 0) ? 8 : 10;
        }
      | number DIGIT {
          $$ = base * $1 + $2;
        };

%%

#include "lex.yy.c"

int main() {
  return yyparse();
}

int yyerror(char *s) {
  fprintf(stderr, "%s\n", s);
  return 1;
}

int yywrap() {
  return 1;
}
