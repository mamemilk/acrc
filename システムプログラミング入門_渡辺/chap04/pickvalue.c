#include <stdio.h>
#include <stdlib.h>

struct y_t{
    int x[50];
};

struct z_t{
    struct y_t y[50];
};

int main(int argc, char *argv[]){
    FILE *fp;

    if(argc != 5){
        fprintf(stderr, "Usage : pickvalue <file> <i> <j> <k>\n");
    }

    int x,y,z;
    char *endptr;
    x = (int)strtol(argv[2], &endptr, 10);
    y = (int)strtol(argv[3], &endptr, 10);
    z = (int)strtol(argv[4], &endptr, 10);

    if((fp=fopen(argv[1], "rb")) == NULL){
        perror(argv[1]);
        exit(EXIT_FAILURE);
    }

    fseek(fp, sizeof(int)*(2500*z + 50*y + x), SEEK_SET);

    int pix;
    fread(&pix, sizeof(int), 1, fp);
    printf("The value of (%d %d %d) is %d\n", x,y,z,pix);

    if(fclose(fp) == EOF){
        perror(argv[1]);
        exit(EXIT_FAILURE);
    }
}