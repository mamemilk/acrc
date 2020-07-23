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
void Exp(void);
void Term(void);
void Exp2(void);

int main(void){
	advance(); Z();
}

void Z(void){
	printf("Z\n");
	Exp(); e0f();
}
void Exp(void){
	printf("Exp\n");
	Term(); Exp2();
}
void Term(void){
	printf("Term\n");
	switch(tok){
		case ID: eat(ID); break;
		case NUM: eat(NUM); break;
		case LPAR: eat(LPAR); Exp(); eat(RPAR);break;
		default: error();
	}
}
void Exp2(void){
	printf("Exp2\n");
	switch(tok){
		case ADD: eat(ADD); Term(); Exp2(); break;
		case SUB: eat(SUB); Term(); Exp2(); break;
		case MUL: eat(MUL); Term(); Exp2(); break;
		case DIV: eat(DIV); Term(); Exp2(); break;
		case RPAR: break;
		default: error();
	}
}
