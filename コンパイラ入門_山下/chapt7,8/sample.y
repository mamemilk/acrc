%token INT  FLOAT  ID  NUM  REAL  COMMA  EQ  EX  QU  SEMI  ADD  SUB  MUL  DIV  LPAR  RPAR  ERROR;

%%
Program     : DAIStmts PrintStmts {}
DAIStmts    : DeclStmt SEMI {}
            | DAIStmts DAIStmt SEMI{}
DAIStmt     : DeclStmt {}
            | AssignStmt {}
            | InputStmt {}
DeclStmt    : Type VarDefs {}
Type        : INT {}
            | FLOAT {}
VarDefs     : VarDef {}
            | VarDefs COMMA VarDef {}
VarDef      : ID {}
            | ID EQ NumReal {}
AssignStmt  : ID EQ Exp {}
InputStmt   : QU VarRefs {}
VarRefs     : ID {}
            | VarRefs COMMA ID {}
PrintStmts  : /* empty */ {}
            | PrintStmts PrintStmt SEMI {}
PrintStmt   : EX Exps {}
Exps        : Exp {}
            | Exps COMMA Exp {}
Exp         : Exp ADD Term {}
            | Exp SUB Term {}
            | Term {}
Term        : Term MUL Factor {}
            | Term DIV Factor {}
            | Factor {}
Factor      : ID {}
            | NumReal {}
            | LPAR Exp RPAR {}
NumReal     : NUM {}
            | REAL {}
%%
#include "lex.yy.c"
int main(){
    if(!yyparse()) printf("successfully ended\n");
}
int yyerror(char* s){printf("%s\n", s); return -1;}

