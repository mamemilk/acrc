#include <stdio.h>
#include <stdlib.h>

struct profile{
    char name[18];
    int age;
    float height;
};

int main(){
    FILE *fp;

    struct profile list[4];

    if((fp=fopen("list_binary.bin", "rb")) == NULL){
        perror("list_binary.bin");
        exit(EXIT_FAILURE);
    }

    int len = fread(list, sizeof(struct profile), 4, fp);

    if(len !=  4){
        fprintf(stderr, "can not read enough data %d / %d", len,  4);
        exit(EXIT_FAILURE);
    }

    for(int i=0;i<4;i++){
        printf("[No.%d] name=%s, age=%d, height=%f\n", 
            i,
            list[i].name,
            list[i].age,
            list[i].height);
    }

    if(fclose(fp) == EOF){
        perror("list_binary.bin");
        exit(EXIT_FAILURE);
    }
}