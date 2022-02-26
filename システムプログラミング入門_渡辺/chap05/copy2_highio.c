#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#define COPYSIZE 256

double getETime(){
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec + (double) tv.tv_usec * 1e-6;
}

int main(int argc, char *argv[]){
    FILE *fpin, *fpout;
    double st, en;
    char c[COPYSIZE];

    if(argc != 3){
        fprintf(stderr, "Usage:copy_highio <source> <destination>\n");
        exit(EXIT_FAILURE);
    }

    if((fpin=fopen(argv[1], "rb")) == NULL){
        perror(argv[1]);
        exit(EXIT_FAILURE);
    }
    if((fpout=fopen(argv[2], "wb")) == NULL){
        perror(argv[2]);
        exit(EXIT_FAILURE);
    }

    st = getETime();
    while( fread(c, 1, COPYSIZE, fpin) == COPYSIZE ){
        fwrite(c, 1, COPYSIZE, fpout);
    }
    en = getETime();

    fclose(fpin);
    fclose(fpout);
    
    printf("Elapsed Time: %.6f\n", en - st);
}