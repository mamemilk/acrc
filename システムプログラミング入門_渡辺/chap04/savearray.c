#include <stdio.h>
#include <stdlib.h>

struct y_t{
    int x[50];
};

struct z_t{
    struct y_t y[50];
};

int main(){
    FILE *fp;

    struct z_t z[50];

    //increment for debug
    for(int zi = 0; zi<50; zi++){
        for(int yi = 0; yi<50; yi++){
            for(int xi = 0; xi<50; xi++){
                z[zi].y[yi].x[xi] = 2500 * zi + 50 * yi + xi;
            }   
        }
    }

    if((fp=fopen("array.bin", "wb")) == NULL){
        perror("array.bin");
        exit(EXIT_FAILURE);
    }

    fwrite(z, sizeof(struct z_t), 50, fp);

    if(fclose(fp) == EOF){
        perror("array.bin");
        exit(EXIT_FAILURE);
    }
}