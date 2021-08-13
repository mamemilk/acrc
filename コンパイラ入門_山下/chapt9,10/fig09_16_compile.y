%token INT FLOAT ID NUM REAL COMMA EQ EX QU  
       SEMI ADD SUB MUL DIV LPAR RPAR ERROR;
%{
#include <string.h>
#include "fig09_04.h"
#include "fig09_09.h"
#include "fig09_20.h"
#define YYSTYPE node*

YYSTYPE myval;

int declType;
%}

%%
Program
  : DeAsInStmts 
              PrintStmts {
      myval = newTProgram(
             $1,
    		 $2);
    }
DeAsInStmts 
  : DeclStmt SEMI
               { $$ = $1; }
  | DeAsInStmts 
		  DeAsInStmt SEMI
    { $$ = append($1,$2); }
DeAsInStmt  
  : DeclStmt   { $$ = $1; }
  | AssignStmt { $$ = $1; }
  | InputStmt  { $$ = $1; }
DeclStmt    
  : Type VarDefs
               { $$ = $2; }
Type        
  : INT 
       { declType = TINT; }
  | FLOAT
	 { declType = TFLOAT; }
VarDefs
  : VarDef {
      $$ = newTDeAsInSeq(
    		 $1,
    		 NULL);
    }
  | VarDefs COMMA VarDef {
      $$ = append(
    		 $1,
    		 newTDeAsInSeq(
    		   $3,
    		   NULL));
    }
VarDef      
  : ID {
      $$ = newTDecl(
    		 $1->name,
    		 declType,
    		 newTInt(0));
    }
  | ID EQ NumReal {
      $$ = newTDecl(
    		 $1->name,
    		 declType,
    		 $3);
    }
AssignStmt  
  : ID EQ Exp {
    $$ = newTDeAsInSeq(
    	   newTAssign(
    		 $1->name,
    		 $3),
    	   NULL);
    }
InputStmt   
  : QU VarRefs { $$ = $2; }
VarRefs     
  : ID {
      $$ = newTDeAsInSeq(
    		 newTInput(
    		   $1->name),
    		 NULL);
    }
  | VarRefs COMMA ID {
      $$ = append(
    		 $1,
    		 newTDeAsInSeq(
    		   newTInput($3->name),
    		   NULL));
    }
PrintStmts  
  : /* empty */
             { $$ = NULL; }
  | PrintStmts 
           PrintStmt SEMI
    { $$ = append($1,$2); }
PrintStmt   
  : EX Exps {
      $$ = 
	    append(
    	  $2,
    	  newTPrintSeq(
    	    newTNewline(),
			NULL));
    }
Exps        
  : Exp {
      $$ = newTPrintSeq(
    		 newTPrint($1),
    		 NULL);
    }
  | Exps COMMA Exp {
      $$ = 
	    append(
    	  $1,
    	  newTPrintSeq(
    	    newTPrint($3),
    		NULL));
    }
Exp
  : Exp ADD Term
    { $$= newTAdd($1,$3); }
  | Exp SUB Term
	{ $$= newTSub($1,$3); }
  | Term       { $$ = $1; }
Term
  : Term MUL Factor
	{ $$= newTMul($1,$3); }
  | Term DIV Factor
    { $$= newTDiv($1,$3); }
  | Factor     { $$ = $1; }
Factor      
  : ID         { $$ = $1; }
  | NumReal    { $$ = $1; }
  | LPAR Exp RPAR
               { $$ = $2; }
NumReal
  : NUM        { $$ = $1; }
  | REAL       { $$ = $1; }
%%
#include "lex.yy.c"

int main(int argc, char *argv[]) {

    if(argc > 1) {
            yyin = fopen(argv[1], "r");
        if(!yyin){
            fprintf(stderr,"fopen error_n"); 
            exit(1); 
        }
    }else {
        fprintf(stderr,"arg error_n"); 
        exit(1);
    }
    if(!yyparse()){
      checkSem(myval);
      insertType(myval);
      printTable();
    	print(myval);

      eval(myval)
    }
    


}
int yyerror(char* s){ fprintf(stderr,"%s_n",s); return 0;}
