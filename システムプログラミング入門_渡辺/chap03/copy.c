#include <stdio.h>
#include <stdlib.h>

#define BUFSIZE 512 

int main(int argc, char *argv[]){
    FILE *fpin, *fpout;
    char buf[BUFSIZE];

    if(argc < 3){
        fprintf(stderr, "Usage : copy <source> <destination>\n");
        exit(EXIT_FAILURE);
    }

    if((fpin=fopen(argv[1], "r")) == NULL){
        perror(argv[1]);
        exit(EXIT_FAILURE);
    }
    if((fpout=fopen(argv[2], "w")) == NULL){
        perror(argv[2]);
        exit(EXIT_FAILURE);
    }

    while(fgets(buf, BUFSIZE-1, fpin) != NULL){
        fputs(buf, fpout);
    }

    if(EOF == fclose(fpin)){
        perror(argv[1]);
        exit(EXIT_FAILURE);
    }
    if(EOF == fclose(fpout)){
        perror(argv[2]);
        exit(EXIT_FAILURE);
    }
}