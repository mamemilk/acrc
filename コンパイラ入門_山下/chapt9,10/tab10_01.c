#include <stdio.h>
#include <stdlib.h>
#include "fig09_04.h"
#include "fig09_09.h"
#include "fig10_01.h"
#include "fig10_03.h"

void checkSem(node* np){
    if(np == NULL) return;
    switch(np->label){
    case TDecl:
        putVar(np->name,np->type);
        break;
    case TInput: case TVar:
        getType(np->name);
        break;
    case TAssign:
        getType(np->name);
        checkSem(np->left);
        break;
    case TPrint:
        checkSem(np->left);
        break;
    case TProgram:
    case TDeAsInSeq:
    case TPrintSeq:
    case TAdd:
    case TSub:
    case TMul:
    case TDiv:
        checkSem(np->left);
        checkSem(np->right);
    }
}

void checkSem_insertType(node* np){
    if(np == NULL) return;
    switch(np->label){
    case TDecl:
        putVar(np->name,np->type);
        np->left = castType(np->left,np->type);
        break;
    
    case TInput: 
    case TVar:
        np->type = getType(np->name); 
        break;

    case TAssign:
        np->type = getType(np->name); 
        checkSem_insertType(np->left); //checkSem(np->left);
        insertType(np->left);
        np->left = castType(np->left,np->type);
        break;

    case TPrint:
        checkSem_insertType(np->left); //insertType(np->left);
        np->type = np->left->type;
        
        break;

    case TProgram:
    case TDeAsInSeq:
    case TPrintSeq:
        checkSem_insertType(np->left);   //insertType(np->left);
        checkSem_insertType(np->right);  //insertType(np->right);
        break;

    case TAdd:
    case TSub:
    case TMul:
    case TDiv:
        checkSem_insertType(np->left);   //insertType(np->left);
        checkSem_insertType(np->right);  //insertType(np->right);

        if(np->left->type == np->right->type) {
            np->type = np->left->type;
        } else {
            np->left = castType(np->left,TFLOAT);
            np->right = castType(np->right,TFLOAT);
            np->type = TFLOAT;
        }

    }
}

