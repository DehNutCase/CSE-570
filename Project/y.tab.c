/* original parser id follows */
/* yysccsid[] = "@(#)yaccpar	1.9 (Berkeley) 02/21/93" */
/* (use YYMAJOR/YYMINOR for ifdefs dependent on parser version) */

#define YYBYACC 1
#define YYMAJOR 1
#define YYMINOR 9
#define YYPATCH 20170709

#define YYEMPTY        (-1)
#define yyclearin      (yychar = YYEMPTY)
#define yyerrok        (yyerrflag = 0)
#define YYRECOVERING() (yyerrflag != 0)
#define YYENOMEM       (-2)
#define YYEOF          0
#define YYPREFIX "yy"

#define YYPURE 0

#line 2 "cal.y"
#include <stdio.h>
int regs[26];
int base;
int yylex();
int yyerror(char *s);
int yywrap();
int last = 0;
#ifdef YYSTYPE
#undef  YYSTYPE_IS_DECLARED
#define YYSTYPE_IS_DECLARED 1
#endif
#ifndef YYSTYPE_IS_DECLARED
#define YYSTYPE_IS_DECLARED 1
#line 12 "cal.y"
typedef union {
  int a;
  char c;
} YYSTYPE;
#endif /* !YYSTYPE_IS_DECLARED */
#line 41 "y.tab.c"

/* compatibility with bison */
#ifdef YYPARSE_PARAM
/* compatibility with FreeBSD */
# ifdef YYPARSE_PARAM_TYPE
#  define YYPARSE_DECL() yyparse(YYPARSE_PARAM_TYPE YYPARSE_PARAM)
# else
#  define YYPARSE_DECL() yyparse(void *YYPARSE_PARAM)
# endif
#else
# define YYPARSE_DECL() yyparse(void)
#endif

/* Parameters sent to lex. */
#ifdef YYLEX_PARAM
# define YYLEX_DECL() yylex(void *YYLEX_PARAM)
# define YYLEX yylex(YYLEX_PARAM)
#else
# define YYLEX_DECL() yylex(void)
# define YYLEX yylex()
#endif

/* Parameters sent to yyerror. */
#ifndef YYERROR_DECL
#define YYERROR_DECL() yyerror(const char *s)
#endif
#ifndef YYERROR_CALL
#define YYERROR_CALL(msg) yyerror(msg)
#endif

extern int YYPARSE_DECL();

#define DIGIT 257
#define LETTER 258
#define UMINUS 259
#define YYERRCODE 256
typedef short YYINT;
static const YYINT yylhs[] = {                           -1,
    0,    0,    0,    3,    3,    3,    3,    3,    3,    3,
    3,    1,    1,    1,    1,    1,    1,    1,    1,    1,
    1,    1,    2,    2,
};
static const YYINT yylen[] = {                            2,
    0,    3,    3,    1,    3,    2,    2,    2,    2,    2,
    2,    3,    3,    3,    3,    3,    3,    3,    3,    2,
    1,    1,    1,    2,
};
static const YYINT yydefred[] = {                         1,
    0,    0,   23,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    3,    0,   21,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
   24,    2,    0,   20,   12,    0,    0,    0,    0,   13,
   14,   15,
};
static const YYINT yydgoto[] = {                          1,
   11,   12,   13,
};
static const YYINT yysindex[] = {                         0,
  -37,   -8,    0,  -57,  -33,  -33,  -33,  -33,  -33,  -33,
   45, -239,   11,    0,  -33,    0,  -33,   45,    0,   45,
   45,   45,   34,  -33,  -33,  -33,  -33,  -33,  -33,  -33,
    0,    0,   45,    0,    0,   86,  -28,  -17,  -17,    0,
    0,    0,
};
static const YYINT yyrindex[] = {                         0,
    0,    0,    0,    3,    0,    0,    0,    0,    0,    0,
   12,   -9,    0,    0,   13,    0,    0,   16,   14,   21,
   27,   33,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,   39,    0,    0,    6,    1,   17,   25,    0,
    0,    0,
};
static const YYINT yygindex[] = {                         0,
   92,    0,    0,
};
#define YYTABLESIZE 225
static const YYINT yytable[] = {                          9,
   22,   14,   10,   15,    7,    5,   10,    6,   30,    8,
   18,   17,   21,   28,   26,   19,   27,   31,   29,   30,
   32,    4,    6,   11,   28,   10,   16,   22,   22,   29,
    7,   22,   22,   22,   17,   22,    8,   22,   18,   21,
   21,   18,    9,    0,   21,   21,   19,   21,    5,   21,
   20,   20,    0,    0,   16,   20,   20,   16,   20,   16,
   20,   16,   17,    0,    0,   17,    0,   17,    0,   17,
   30,   25,    0,    0,   35,   28,   26,    0,   27,    0,
   29,   30,   25,    0,    0,    0,   28,   26,    0,   27,
    0,   29,    0,    0,    0,    0,   18,   19,   20,   21,
   22,   23,    0,    0,    0,    0,   33,    0,   34,    0,
    0,    0,    0,    0,   22,   36,   37,   38,   39,   40,
   41,   42,   30,   25,   18,    0,   21,   28,   26,   19,
   27,    0,   29,    0,    0,    0,    0,   20,    0,    0,
   16,    0,    0,    0,    0,    0,    0,    0,   17,    0,
    0,    0,    0,    0,    0,    0,    0,   24,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,   24,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    2,    3,
    4,    0,    0,    3,   16,
};
static const YYINT yycheck[] = {                         37,
   10,   10,   40,   61,   42,   43,   40,   45,   37,   47,
   10,   45,   10,   42,   43,   10,   45,  257,   47,   37,
   10,   10,   10,   10,   42,   10,   10,   37,   38,   47,
   10,   41,   42,   43,   10,   45,   10,   47,   38,   37,
   38,   41,   10,   -1,   42,   43,   41,   45,   10,   47,
   37,   38,   -1,   -1,   38,   42,   43,   41,   45,   43,
   47,   45,   38,   -1,   -1,   41,   -1,   43,   -1,   45,
   37,   38,   -1,   -1,   41,   42,   43,   -1,   45,   -1,
   47,   37,   38,   -1,   -1,   -1,   42,   43,   -1,   45,
   -1,   47,   -1,   -1,   -1,   -1,    5,    6,    7,    8,
    9,   10,   -1,   -1,   -1,   -1,   15,   -1,   17,   -1,
   -1,   -1,   -1,   -1,  124,   24,   25,   26,   27,   28,
   29,   30,   37,   38,  124,   -1,  124,   42,   43,  124,
   45,   -1,   47,   -1,   -1,   -1,   -1,  124,   -1,   -1,
  124,   -1,   -1,   -1,   -1,   -1,   -1,   -1,  124,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,  124,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,  124,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,  256,  257,
  258,   -1,   -1,  257,  258,
};
#define YYFINAL 1
#ifndef YYDEBUG
#define YYDEBUG 0
#endif
#define YYMAXTOKEN 259
#define YYUNDFTOKEN 265
#define YYTRANSLATE(a) ((a) > YYMAXTOKEN ? YYUNDFTOKEN : (a))
#if YYDEBUG
static const char *const yyname[] = {

"end-of-file",0,0,0,0,0,0,0,0,0,"'\\n'",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,"'%'","'&'",0,"'('","')'","'*'","'+'",0,"'-'",0,"'/'",0,0,0,0,0,0,0,
0,0,0,0,0,0,"'='",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"'|'",0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,"DIGIT","LETTER","UMINUS",0,0,0,0,0,"illegal-symbol",
};
static const char *const yyrule[] = {
"$accept : list",
"list :",
"list : list stat '\\n'",
"list : list error '\\n'",
"stat : expr",
"stat : LETTER '=' expr",
"stat : LETTER '='",
"stat : '*' expr",
"stat : '/' expr",
"stat : '%' expr",
"stat : '+' expr",
"stat : '-' expr",
"expr : '(' expr ')'",
"expr : expr '*' expr",
"expr : expr '/' expr",
"expr : expr '%' expr",
"expr : expr '+' expr",
"expr : expr '-' expr",
"expr : expr '&' expr",
"expr : expr '|' expr",
"expr : '-' expr",
"expr : LETTER",
"expr : number",
"number : DIGIT",
"number : number DIGIT",

};
#endif

int      yydebug;
int      yynerrs;

int      yyerrflag;
int      yychar;
YYSTYPE  yyval;
YYSTYPE  yylval;

/* define the initial stack-sizes */
#ifdef YYSTACKSIZE
#undef YYMAXDEPTH
#define YYMAXDEPTH  YYSTACKSIZE
#else
#ifdef YYMAXDEPTH
#define YYSTACKSIZE YYMAXDEPTH
#else
#define YYSTACKSIZE 10000
#define YYMAXDEPTH  10000
#endif
#endif

#define YYINITSTACKSIZE 200

typedef struct {
    unsigned stacksize;
    YYINT    *s_base;
    YYINT    *s_mark;
    YYINT    *s_last;
    YYSTYPE  *l_base;
    YYSTYPE  *l_mark;
} YYSTACKDATA;
/* variables for the parser stack */
static YYSTACKDATA yystack;
#line 124 "cal.y"

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
#line 265 "y.tab.c"

#if YYDEBUG
#include <stdio.h>	/* needed for printf */
#endif

#include <stdlib.h>	/* needed for malloc, etc */
#include <string.h>	/* needed for memset */

/* allocate initial stack or double stack size, up to YYMAXDEPTH */
static int yygrowstack(YYSTACKDATA *data)
{
    int i;
    unsigned newsize;
    YYINT *newss;
    YYSTYPE *newvs;

    if ((newsize = data->stacksize) == 0)
        newsize = YYINITSTACKSIZE;
    else if (newsize >= YYMAXDEPTH)
        return YYENOMEM;
    else if ((newsize *= 2) > YYMAXDEPTH)
        newsize = YYMAXDEPTH;

    i = (int) (data->s_mark - data->s_base);
    newss = (YYINT *)realloc(data->s_base, newsize * sizeof(*newss));
    if (newss == 0)
        return YYENOMEM;

    data->s_base = newss;
    data->s_mark = newss + i;

    newvs = (YYSTYPE *)realloc(data->l_base, newsize * sizeof(*newvs));
    if (newvs == 0)
        return YYENOMEM;

    data->l_base = newvs;
    data->l_mark = newvs + i;

    data->stacksize = newsize;
    data->s_last = data->s_base + newsize - 1;
    return 0;
}

#if YYPURE || defined(YY_NO_LEAKS)
static void yyfreestack(YYSTACKDATA *data)
{
    free(data->s_base);
    free(data->l_base);
    memset(data, 0, sizeof(*data));
}
#else
#define yyfreestack(data) /* nothing */
#endif

#define YYABORT  goto yyabort
#define YYREJECT goto yyabort
#define YYACCEPT goto yyaccept
#define YYERROR  goto yyerrlab

int
YYPARSE_DECL()
{
    int yym, yyn, yystate;
#if YYDEBUG
    const char *yys;

    if ((yys = getenv("YYDEBUG")) != 0)
    {
        yyn = *yys;
        if (yyn >= '0' && yyn <= '9')
            yydebug = yyn - '0';
    }
#endif

    yym = 0;
    yyn = 0;
    yynerrs = 0;
    yyerrflag = 0;
    yychar = YYEMPTY;
    yystate = 0;

#if YYPURE
    memset(&yystack, 0, sizeof(yystack));
#endif

    if (yystack.s_base == NULL && yygrowstack(&yystack) == YYENOMEM) goto yyoverflow;
    yystack.s_mark = yystack.s_base;
    yystack.l_mark = yystack.l_base;
    yystate = 0;
    *yystack.s_mark = 0;

yyloop:
    if ((yyn = yydefred[yystate]) != 0) goto yyreduce;
    if (yychar < 0)
    {
        yychar = YYLEX;
        if (yychar < 0) yychar = YYEOF;
#if YYDEBUG
        if (yydebug)
        {
            if ((yys = yyname[YYTRANSLATE(yychar)]) == NULL) yys = yyname[YYUNDFTOKEN];
            printf("%sdebug: state %d, reading %d (%s)\n",
                    YYPREFIX, yystate, yychar, yys);
        }
#endif
    }
    if (((yyn = yysindex[yystate]) != 0) && (yyn += yychar) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == (YYINT) yychar)
    {
#if YYDEBUG
        if (yydebug)
            printf("%sdebug: state %d, shifting to state %d\n",
                    YYPREFIX, yystate, yytable[yyn]);
#endif
        if (yystack.s_mark >= yystack.s_last && yygrowstack(&yystack) == YYENOMEM) goto yyoverflow;
        yystate = yytable[yyn];
        *++yystack.s_mark = yytable[yyn];
        *++yystack.l_mark = yylval;
        yychar = YYEMPTY;
        if (yyerrflag > 0)  --yyerrflag;
        goto yyloop;
    }
    if (((yyn = yyrindex[yystate]) != 0) && (yyn += yychar) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == (YYINT) yychar)
    {
        yyn = yytable[yyn];
        goto yyreduce;
    }
    if (yyerrflag != 0) goto yyinrecovery;

    YYERROR_CALL("syntax error");

    goto yyerrlab; /* redundant goto avoids 'unused label' warning */
yyerrlab:
    ++yynerrs;

yyinrecovery:
    if (yyerrflag < 3)
    {
        yyerrflag = 3;
        for (;;)
        {
            if (((yyn = yysindex[*yystack.s_mark]) != 0) && (yyn += YYERRCODE) >= 0 &&
                    yyn <= YYTABLESIZE && yycheck[yyn] == (YYINT) YYERRCODE)
            {
#if YYDEBUG
                if (yydebug)
                    printf("%sdebug: state %d, error recovery shifting\
 to state %d\n", YYPREFIX, *yystack.s_mark, yytable[yyn]);
#endif
                if (yystack.s_mark >= yystack.s_last && yygrowstack(&yystack) == YYENOMEM) goto yyoverflow;
                yystate = yytable[yyn];
                *++yystack.s_mark = yytable[yyn];
                *++yystack.l_mark = yylval;
                goto yyloop;
            }
            else
            {
#if YYDEBUG
                if (yydebug)
                    printf("%sdebug: error recovery discarding state %d\n",
                            YYPREFIX, *yystack.s_mark);
#endif
                if (yystack.s_mark <= yystack.s_base) goto yyabort;
                --yystack.s_mark;
                --yystack.l_mark;
            }
        }
    }
    else
    {
        if (yychar == YYEOF) goto yyabort;
#if YYDEBUG
        if (yydebug)
        {
            if ((yys = yyname[YYTRANSLATE(yychar)]) == NULL) yys = yyname[YYUNDFTOKEN];
            printf("%sdebug: state %d, error recovery discards token %d (%s)\n",
                    YYPREFIX, yystate, yychar, yys);
        }
#endif
        yychar = YYEMPTY;
        goto yyloop;
    }

yyreduce:
#if YYDEBUG
    if (yydebug)
        printf("%sdebug: state %d, reducing by rule %d (%s)\n",
                YYPREFIX, yystate, yyn, yyrule[yyn]);
#endif
    yym = yylen[yyn];
    if (yym > 0)
        yyval = yystack.l_mark[1-yym];
    else
        memset(&yyval, 0, sizeof yyval);

    switch (yyn)
    {
case 3:
#line 29 "cal.y"
	{
      yyerrok;
    }
break;
case 4:
#line 33 "cal.y"
	{
        printf("%d\n", yystack.l_mark[0].a);
        last = yystack.l_mark[0].a; /* We memorize the last result.*/
      }
break;
case 5:
#line 37 "cal.y"
	{
      /* KL, this is what stores a value to a variable 
      Note that variables are single characters, lowercase
      due to their definition in cal.l 
      
      That is, this is the form of the assignment statement.
      */
      regs[yystack.l_mark[-2].c] = yystack.l_mark[0].a;
    }
break;
case 6:
#line 46 "cal.y"
	{
      /* KL, We allow storing variables from the last result.
      Typing LETTER = will cause LETTER to have the value of
      the last result.
      
      Note that last is initiated to 0 to prevent errors.
      */
      regs[yystack.l_mark[-1].c] = last;
    }
break;
case 7:
#line 55 "cal.y"
	{
        /* This is what uses the last result to calculate
        the next.
        
        That is, this is the form of the exit/quit feature
        (Since it doesn't start with an expr, we assume
        the first expr is simply the last value)
        */
        last = last * yystack.l_mark[0].a;
        printf("%d\n", last);
      }
break;
case 8:
#line 66 "cal.y"
	{
        last = last / yystack.l_mark[0].a;
        printf("%d\n", last);
      }
break;
case 9:
#line 70 "cal.y"
	{
        last = last % yystack.l_mark[0].a;
        printf("%d\n", last);
      }
break;
case 10:
#line 74 "cal.y"
	{
        last = last + yystack.l_mark[0].a;
        printf("%d\n", last);
      }
break;
case 11:
#line 78 "cal.y"
	{
        last = last - yystack.l_mark[0].a;
        printf("%d\n", last);
      }
break;
case 12:
#line 83 "cal.y"
	{
        yyval.a = yystack.l_mark[-1].a;
      }
break;
case 13:
#line 86 "cal.y"
	{
        yyval.a = yystack.l_mark[-2].a * yystack.l_mark[0].a;
      }
break;
case 14:
#line 89 "cal.y"
	{
        yyval.a = yystack.l_mark[-2].a / yystack.l_mark[0].a;
      }
break;
case 15:
#line 92 "cal.y"
	{
        yyval.a = yystack.l_mark[-2].a % yystack.l_mark[0].a;
      }
break;
case 16:
#line 95 "cal.y"
	{
        yyval.a = yystack.l_mark[-2].a + yystack.l_mark[0].a;
      }
break;
case 17:
#line 98 "cal.y"
	{
        yyval.a = yystack.l_mark[-2].a - yystack.l_mark[0].a;
      }
break;
case 18:
#line 101 "cal.y"
	{
        yyval.a = yystack.l_mark[-2].a & yystack.l_mark[0].a;
      }
break;
case 19:
#line 104 "cal.y"
	{
        yyval.a = yystack.l_mark[-2].a | yystack.l_mark[0].a;
      }
break;
case 20:
#line 107 "cal.y"
	{
        yyval.a = -yystack.l_mark[0].a;
      }
break;
case 21:
#line 110 "cal.y"
	{
        yyval.a = regs[yystack.l_mark[0].c];
      }
break;
case 23:
#line 115 "cal.y"
	{
          yyval.a = yystack.l_mark[0].a;
          base = (yystack.l_mark[0].a == 0) ? 8 : 10;
        }
break;
case 24:
#line 119 "cal.y"
	{
          yyval.a = base * yystack.l_mark[-1].a + yystack.l_mark[0].a;
        }
break;
#line 616 "y.tab.c"
    }
    yystack.s_mark -= yym;
    yystate = *yystack.s_mark;
    yystack.l_mark -= yym;
    yym = yylhs[yyn];
    if (yystate == 0 && yym == 0)
    {
#if YYDEBUG
        if (yydebug)
            printf("%sdebug: after reduction, shifting from state 0 to\
 state %d\n", YYPREFIX, YYFINAL);
#endif
        yystate = YYFINAL;
        *++yystack.s_mark = YYFINAL;
        *++yystack.l_mark = yyval;
        if (yychar < 0)
        {
            yychar = YYLEX;
            if (yychar < 0) yychar = YYEOF;
#if YYDEBUG
            if (yydebug)
            {
                if ((yys = yyname[YYTRANSLATE(yychar)]) == NULL) yys = yyname[YYUNDFTOKEN];
                printf("%sdebug: state %d, reading %d (%s)\n",
                        YYPREFIX, YYFINAL, yychar, yys);
            }
#endif
        }
        if (yychar == YYEOF) goto yyaccept;
        goto yyloop;
    }
    if (((yyn = yygindex[yym]) != 0) && (yyn += yystate) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == (YYINT) yystate)
        yystate = yytable[yyn];
    else
        yystate = yydgoto[yym];
#if YYDEBUG
    if (yydebug)
        printf("%sdebug: after reduction, shifting from state %d \
to state %d\n", YYPREFIX, *yystack.s_mark, yystate);
#endif
    if (yystack.s_mark >= yystack.s_last && yygrowstack(&yystack) == YYENOMEM) goto yyoverflow;
    *++yystack.s_mark = (YYINT) yystate;
    *++yystack.l_mark = yyval;
    goto yyloop;

yyoverflow:
    YYERROR_CALL("yacc stack overflow");

yyabort:
    yyfreestack(&yystack);
    return (1);

yyaccept:
    yyfreestack(&yystack);
    return (0);
}
