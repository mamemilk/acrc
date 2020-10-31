%{

#include <string.h>

typedef struct _node {
    int           label;
    int           type;
    char         *name;
    int           ival;
    float         fval;
    struct _node *left;
    struct _node *right;
} node;
enum{TINT, TFLOAT};

enum{
    TProgram,
    TDAISeq, 
    TDecl,
    TAssign,
    TInput,
    TPrintSeq,
    TPrint,
    TNewline,
    TAdd,
    TSub,
    TMul,
    TDiv,
    TVar,
    TInt,
    TFloat
};

node *newTProgram  (                                            node *left, node *right);              
node *newTDAISeq   (                                            node *left, node *right);             
node *newTDecl     (int type, char *name,                       node *left             );           
node *newTAssign   (int type, char *name, int ival, float fval, node *left, node *right);             
node *newTInput    (int type, char *name, int ival, float fval, node *left, node *right);            
node *newTPrintSeq (int type, char *name, int ival, float fval, node *left, node *right);               
node *newTPrint    (int type, char *name, int ival, float fval, node *left, node *right);            
node *newTNewline  (int type, char *name, int ival, float fval, node *left, node *right);              
node *newTAdd      (int type, char *name, int ival, float fval, node *left, node *right);          
node *newTSub      (int type, char *name, int ival, float fval, node *left, node *right);          
node *newTMul      (int type, char *name, int ival, float fval, node *left, node *right);          
node *newTDiv      (int type, char *name, int ival, float fval, node *left, node *right);          
node *newTVar      (char *name);          
node *newTInt      (int type, char *name, int ival, float fval, node *left, node *right);          
node *newTFloat    (int type, char *name, int ival, float fval, node *left, node *right);           

node *newnode(int label, int type, 
              char *name, int ival, float fval, 
              node *left, node *right){
    node *np = (node*)malloc(sizeof(node));
    np->label = label;        
    np->type  = type ;       
    np->name  = name ;       
    np->ival  = ival ;       
    np->fval  = fval ;       
    np->left  = left ;       
    np->right = right;        
    return np;
}

node *newTVar      (char *name){
    return newnode(TVar, -1, 
                   name, 0, 0, 
                   NULL, NULL);
}

node *lval; //意味値受け渡し用  

enum {INT=1, FLOAT, ID, NUM, REAL, COMMA, EQ, EX, QU, SEMI, ADD, SUB, MUL, DIV, LPAR, RPAR, ERROR};

%}
%%
int                                 {return INT;    }
float                               {return FLOAT;  }
[a-z][a-z0-9]*                      {lval = newTVar(strdup(yytext));
                                     return ID;     }
0|[1-9][0-9]*                       {return NUM;    }
([0-9]+"."[0-9]*)|([0-9]*"."[0-9]+) {return REAL;   }
","                                 {return COMMA;  }
"="                                 {return EQ;     }
"!"                                 {return EX;     }
"?"                                 {return QU;     }
";"                                 {return SEMI;   }
"+"                                 {return ADD;    }
"-"                                 {return SUB;    }
"*"                                 {return MUL;    }
"/"                                 {return DIV;    }
"("                                 {return LPAR;   }
")"                                 {return RPAR;   }
"\n"|" "|"\t"                       { }
"/*"[a-z0-9]*"*/"                   { }
.                                   {return ERROR;  }
%%









int yywrap(void){return 1;}
int main(void){
    int t;
    while((t=yylex()) != 0){
        printf("number = %d, string '%s'\n", t, yytext);
    }
}