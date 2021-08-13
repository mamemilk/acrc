#include <stdio.h>
#include <stdlib.h>
#include "fig09_04.h"
#include "fig09_09.h"
#include "fig10_01.h"
#include "fig10_03.h"
#include "tab11.h"

FILE *code;

int genExp(node *np){
static int iregnum = 1;
static int fregnum = 1;
    int left,right;
    switch(np->label){
    case TAdd:
        left = genExp(np->left);
        right = genExp(np->right);
        if(np->type == TINT){
            fprintf(code,"add.i r%d = r%d,r%d_n",iregnum,left,right);
            return iregnum++;
        }else{
            fprintf(code,"add.f f%d = f%d,f%d_n",fregnum,left,right);
            return fregnum++;
        }
    case TSub:
        left = genExp(np->left);
        right = genExp(np->right);
        if(np->type == TINT){
            fprintf(code,"sub.i r%d = r%d,r%d_n",iregnum,left,right);
            return iregnum++;
        }else{
            fprintf(code,"sub.f f%d = f%d,f%d_n",fregnum,left,right);
            return fregnum++;
        }
    case TMul:
        left = genExp(np->left);
        right = genExp(np->right);
        if(np->type == TINT){
            fprintf(code,"mul.i r%d = r%d,r%d_n",iregnum,left,right);
            return iregnum++;
        }else{
            fprintf(code,"mul.f f%d = f%d,f%d_n",fregnum,left,right);
            return fregnum++;
        }
    case TDiv:
        left = genExp(np->left);
        right = genExp(np->right);
        if(np->type == TINT){
            fprintf(code,"div.i r%d = r%d,r%d_n",iregnum,left,right);
            return iregnum++;
        }else{
            fprintf(code,"div.f f%d = f%d,f%d_n",fregnum,left,right);
            return fregnum++;
        }
    case TVar:
        if(np->type == TINT) {
            fprintf(code,"load.i r%d = [&%s]_n",iregnum,np->name);
            return iregnum++;
        }else{
            fprintf(code,"load.f f%d = [&%s]_n",fregnum,np->name);
            return fregnum++;
        }
    case TInt:
        fprintf(code,"const.i r%d = %d_n",iregnum,np->ival);
        return iregnum++;
    case TFloat:
        fprintf(code,"const.f f%d = %f_n",fregnum,np->fval);
        return fregnum++;
    case TI2F:
        fprintf(code,"conv.fi f%d = r%d_n",fregnum,genExp(np->left));
        return fregnum++;
    case TF2I:
        fprintf(code,"conv.if r%d = f%d_n",iregnum,genExp(np->left));
        return iregnum++;
    }
}
