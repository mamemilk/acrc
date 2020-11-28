#include <stdio.h>
#include <stdlib.h>
#include "fig09_04.h"
#include "fig09_09.h"
#include "fig10_01.h"
#include "fig10_03.h"

void insertType(node *np){
    if(np == NULL) return;
    switch(np->label){
    case TDecl:
        np->left = castType(np->left,np->type);
        break;
    case TInput: case TVar:
        np->type = getType(np->name);
        break;

    case TAssign:
        np->type = getType(np->name);
        insertType(np->left);
        np->left = castType(np->left,np->type);
        break;
        
    case TPrint:
        insertType(np->left);
        np->type = np->left->type;
        break;
    case TProgram: case TDeAsInSeq: case TPrintSeq:
        insertType(np->left);
        insertType(np->right);
        break;
    case TAdd: case TSub: case TMul: case TDiv:
        insertType(np->left);
        insertType(np->right);
        if(np->left->type == np->right->type) {
            np->type = np->left->type;
        } else {
            np->left = castType(np->left,TFLOAT);
            np->right = castType(np->right,TFLOAT);
            np->type = TFLOAT;
        }
    }
}
