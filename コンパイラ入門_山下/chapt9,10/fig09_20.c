#include <stdio.h>
#include <stdlib.h>

#include "fig09_04.h"
#include "fig09_09.h"
#include "fig09_20.h"
#include "fig10_03.h"

void printSpc(int d){
    int i;
    for(i = 0; i < d; i++) putchar(' ');
}

char* getStrType(node* np){
    if(np->type  < 0) return "?";
    else if(np->type == TINT) return "I";
    else if(np->type == TFLOAT) return "F";
    else { fprintf(stderr,"ERROR 10_n"); exit(1); }
}

void print(node *np){ print2(np,0);}
void print2(node *np, int d){
    if(np == NULL){
        printSpc(d); printf("->NULL_n");
    }else{
        switch(np->label){
        case TProgram:
            printSpc(d); printf("->TProgram_n");
            print2(np->left,d+2);
            print2(np->right,d+2);
            break;
        case TDeAsInSeq:
            printSpc(d); printf("->TDeAsInSeq_n");
            print2(np->left,d+2);
            print2(np->right,d+2);
            break;
        case TDecl:
            printSpc(d); printf("->TDecl(%s,%s)_n",getStrType(np),np->name);
            print2(np->left,d+2);
            break;
        case TAssign:
            printSpc(d); printf("->TAssign(%s,%s)_n",getStrType(np),np->name);
            print2(np->left,d+2);
            break;
        case TInput:
            printSpc(d); printf("->TInput(%s,%s)_n",getStrType(np),np->name);
            break;
        case TPrintSeq:
            printSpc(d); printf("->TPrintSeq_n");
            print2(np->left,d+2);
            print2(np->right,d+2);
            break;
        case TPrint:
            printSpc(d); printf("->TPrint(%s)_n",getStrType(np));
            print2(np->left,d+2);
            break;
        case TNewline:
            printSpc(d); printf("->TNewline_n");
            break;
        case TAdd:
            printSpc(d); printf("->TAdd(%s)_n",getStrType(np));
            print2(np->left,d+2);
            print2(np->right,d+2);
            break;
        case TSub:
            printSpc(d); printf("->TSub(%s)_n",getStrType(np));
            print2(np->left,d+2);
            print2(np->right,d+2);
            break;
        case TMul:
            printSpc(d); printf("->TMul(%s)_n",getStrType(np));
            print2(np->left,d+2);
            print2(np->right,d+2);
            break;
        case TDiv:
            printSpc(d); printf("->TDiv(%s)_n",getStrType(np));
            print2(np->left,d+2);
            print2(np->right,d+2);
            break;
        case TVar:
            printSpc(d); printf("->TVar(%s,%s)_n",getStrType(np),np->name);
            break;
        case TInt:
            printSpc(d); printf("->TInt(%s,%d)_n",getStrType(np),np->ival);
            break;
        case TFloat:
            printSpc(d); printf("->TFloat(%s,%f)_n",getStrType(np),np->fval);
            break;
        case TI2F:
            printSpc(d); printf("->TI2F(F)_n");
            print2(np->left,d+2);
            break;
        case TF2I:
            printSpc(d); printf("->TF2I(I)_n");
            print2(np->left,d+2);
            break;
        default:
            fprintf(stderr,"i-tree error %d_n",np->label);
            exit(1);
        }
    }
}
