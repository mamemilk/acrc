#include <stdio.h>
#include <stdlib.h>
#include "fig09_04.h"
#include "fig09_09.h"
#include "fig10_01.h"
#include "fig10_03.h"
#include "tab11.h"

void eval(node *np){
    node *left;
    static int numPrint = 0;
    if(np == NULL) return;
    switch(np->label){
    case TProgram: case TDeAsInSeq: case TPrintSeq:
        eval(np->left);
        eval(np->right);
        break;
    case TDecl: case TAssign:
        updateVar(np->name,evalExp(np->left));
        break;
    case TInput:
        if(np->type == TINT){
            int i;
            scanf("%d",&i);
            updateVar(np->name,newTInt(i));
        }else{
            float f;
            scanf("%f",&f);
            updateVar(np->name,newTFloat(f));
        }
        break;
    case TPrint:
        if(numPrint++ > 0) printf(",");
        left = evalExp(np->left);
        if(np->type == TINT) printf("%d",left->ival);
        else printf("%f",left->fval);
        break;
    case TNewline:
        printf("_n");
        numPrint = 0;
    }
}
