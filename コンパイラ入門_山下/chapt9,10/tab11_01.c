#include <stdio.h>
#include <stdlib.h>
#include "fig09_04.h"
#include "fig09_09.h"
#include "fig10_01.h"
#include "fig10_03.h"
#include "tab11.h"

node *evalExp(node *np){
    node *left,*right;
    switch(np->label){
    case TAdd:
        left = evalExp(np->left);
        right = evalExp(np->right);
        if(np->type == TINT)
            return newTInt(left->ival + right->ival);
        else
            return newTFloat(left->fval + right->fval);
    case TSub:
        left = evalExp(np->left);
        right = evalExp(np->right);
        if(np->type == TINT)
            return newTInt(left->ival - right->ival);
        else
            return newTFloat(left->fval - right->fval);
    case TMul:
        left = evalExp(np->left);
        right = evalExp(np->right);
        if(np->type == TINT)
            return newTInt(left->ival * right->ival);
        else
            return newTFloat(left->fval * right->fval);
    case TDiv:
        left = evalExp(np->left);
        right = evalExp(np->right);
        if(np->type == TINT)
            return newTInt(left->ival / right->ival);
        else
            return newTFloat(left->fval / right->fval);
    case TVar:
        return getVal(np->name);
    case TInt:
    case TFloat:
        return np;
    case TI2F:
        left = evalExp(np->left);
        return newTFloat((float)left->ival);
    case TF2I:
        left = evalExp(np->left);
        return newTInt((int)left->fval);
    }
}

