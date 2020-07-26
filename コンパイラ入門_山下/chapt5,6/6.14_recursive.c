#include <stdio.h>
#include <stdlib.h>

#include "lex.yy.h"
enum {INT = 1, FLOAT, ID, NUM, REAL, COMMA, EQ, EX, QU, SEMI, ADD, SUB, MUL, DIV, LPAR, RPAR, ERROR};

void error(void){ printf("syntax error\n"); exit(1);}
int tok;

void advance(void){
	// while((tok=yylex()) != 0){
    //     printf("number = %d, string '%s'\n", tok, yytext);
    // }
	tok = yylex(); 
	printf("number = %d, string '%s'\n", tok, yytext);
}

void eat(int t){
	if(tok == t){
		advance();
	}else{
		error();
	}
}

void e0f(void){
	if(tok != EOF){
		error();
	}
}

void Z(void);
void Program(void);
void DeclStmts(void);
void DeclStmts2(void);
void DeclStmt(void);
void VarDefs(void);
void VarDefs2(void);
void PrintStmts(void);
void PrintStmt(void);
void VarRefs(void);
void VarRefs2(void);


int main(void){
	advance(); Z();
}

void Z(void){
    Program(); e0f();
}

void Program(void){
    DeclStmts(); PrintStmts();
}
void DeclStmts(void){
    DeclStmt(); eat(SEMI); DeclStmts2();
}
void DeclStmts2(void){
    switch(tok){
		case EX: 
		case EOF: break; 
		case INT: DeclStmts(); break;
		default: error();
	}
}
void DeclStmt(void){
    eat(INT); VarDefs();
}
void VarDefs(void){
    eat(ID); eat(EQ); eat(NUM); VarDefs2();
}
void VarDefs2(void){
    switch(tok){
		case COMMA: eat(COMMA); eat(ID); eat(EQ); eat(NUM);
                    VarDefs2(); break;
		case SEMI: break; 
		default: error();
	}
}
void PrintStmts(void){
    switch(tok){
		case EX: PrintStmt(); eat(SEMI); PrintStmts(); break;
		case EOF: break; 
		default: error();
	}
}
void PrintStmt(void){
    eat(EX); VarRefs();
}
void VarRefs(void){
    eat(ID); VarRefs2();
}
void VarRefs2(void){
        switch(tok){
		case COMMA: eat(COMMA); eat(ID); VarRefs2(); break;
		case SEMI: break; 
		default: error();
	}
}
