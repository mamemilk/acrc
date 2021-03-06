#include <stdio.h>
#include <stdlib.h>
#include "fig09_04.h"
#include "fig09_09.h"
#include "fig10_01.h"

char *STname[N];
int   STtype[N];
node  *STval[N];
int   STidx = 0;

void putVar(char* name, int type){
    int i;
    for(i = 0; i < STidx; i++){
        if(strcmp(name,STname[i]) == 0){
            fprintf(stderr,
                    "multiple declaration: %s\n",name); 
            exit(1); 
        }
    }
    if(STidx == N){
        fprintf(stderr,"symbol table overflow\n"); 
        exit(1);
    }
    STname[STidx] = name;
    STtype[STidx] = type;
    STidx++;
}
int getType(char* name){
    int i;
    for(i = 0; i < STidx; i++){
        if(strcmp(name,STname[i]) == 0) return STtype[i];
    }
    fprintf(stderr,"no declaration: %s\n",name);
    exit(1);
}
node *getVal(char* name){
    int i;
    for(i = 0; i < STidx; i++){
        if(strcmp(name,STname[i]) == 0) return STval[i];
    }
    fprintf(stderr,"no declaration: %s\n",name);
    exit(1);
}
void updateVar(char* name, node *val){
    int i;
    for(i = 0; i < STidx; i++){
        if(strcmp(name,STname[i]) == 0) {
            STval[i] = val;
            return;
        }
    }
    fprintf(stderr,"no declaration: %s\n",name);
    exit(1);
}

void printTable(){
    int i;
    for(i = 0; i < STidx; i++){
    switch(STtype[i]){
    case TINT: printf("%d : int %s\n",i,STname[i]); break;
    case TFLOAT: printf("%d : float %s\n",i,STname[i]); break;
    default: fprintf(stderr,"ERROR: printTable %d\n",STtype[i]); exit(1);
    }
    }
}

