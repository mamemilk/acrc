%token INT  FLOAT  ID  NUM  REAL  COMMA  EQ  EX  QU  SEMI  ADD  SUB  MUL  DIV  LPAR  RPAR  ERROR;
%{
#include "../"
}%

%%
Program     : Exp {}
Exp         : Exp ADD Term {}
            | Exp SUB Term {}
            | Term {}
Term        : Term MUL Factor {}
            | Term DIV Factor {}
            | Factor {}
Factor      : ID {}
            | NUM {}
            | LPAR Exp RPAR {}
%%
#include "lex.yy.c"
int main(){
    if(!yyparse()) printf("successfully ended\n");
}
int yyerror(char* s){printf("%s\n", s); return -1;}

