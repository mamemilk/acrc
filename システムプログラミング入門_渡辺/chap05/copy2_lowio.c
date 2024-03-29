#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/time.h>

#define COPYSIZE 256

double getETime(){
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec + (double) tv.tv_usec * 1e-6;
}

int main(int argc, char *argv[]){
    int fdin, fdout;
    char c[COPYSIZE];
    double st, en;

    if(argc != 3){
        fprintf(stderr, "Usage: ./copy_lowio <source> <destination>\n");
        exit(EXIT_FAILURE);
    }

    if((fdin = open(argv[1], O_RDONLY)) < 0 ){
        perror(argv[1]);
        exit(EXIT_FAILURE);
    }

    if((fdout = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0666)) < 0){
        perror(argv[2]);
        exit(EXIT_FAILURE);
    }

    st = getETime();
    while(read(fdin, c, COPYSIZE) == COPYSIZE){
        write(fdout, c, COPYSIZE);
    }
    en = getETime();
    close(fdin);
    close(fdout);

    printf("Elapsed Time: %.6f\n", en - st);
}
