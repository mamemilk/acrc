#include <stdio.h>
#include <stdlib.h>
#include "fig09_04.h"
#include "fig09_09.h"
#include "fig10_01.h"
#include "fig10_03.h"
#include "tab11.h"

void gen(node *np){
    int left;
    static int numPrint = 0;
    if(np == NULL) return;
    switch(np->label){
    case TProgram: case TDeAsInSeq: case TPrintSeq:
        gen(np->left);
        gen(np->right);
        break;
    case TDecl:
    case TAssign:
        if(np->type == TINT){
            fprintf(code,"store.i [&%s] = r%d_n",np->name,genExp(np->left));
        }else{
            fprintf(code,"store.f [&%s] = f%d_n",np->name,genExp(np->left));
        }
        break;
    case TInput:
        if(np->type == TINT){
            fprintf(code,"call in_int_n");
            fprintf(code,"store.i [&%s] = r0_n",np->name);
        }else{
            fprintf(code,"call in_float_n");
            fprintf(code,"store.f [&%s] = f0_n",np->name);
        }
        break;
    case TPrint:
        if(numPrint++ > 0) fprintf(code,"call out_comma_n");
        left = genExp(np->left);
        if(np->type == TINT){
            fprintf(code,"move.i r0 = r%d_n",left);
            fprintf(code,"call out_int_n");
        }else{
            fprintf(code,"move.f f0 = f%d_n",left);
            fprintf(code,"call out_float_n");
        }
        break;
    case TNewline:
        fprintf(code,"call out_newline_n");
        numPrint = 0;
    }
}
