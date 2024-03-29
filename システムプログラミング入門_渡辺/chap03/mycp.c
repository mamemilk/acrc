#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    FILE *fpin, *fpout;
    char buf;

    if(argc != 3){
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

    while((buf = fgetc(fpin)) != EOF){
        if(fputc(buf, fpout) == EOF){
            perror(argv[2]);
            exit(EXIT_FAILURE);
        }
    }

    if(ferror(fpin) != 0){
        perror(argv[1]);
        exit(EXIT_FAILURE);
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