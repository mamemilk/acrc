#include <stdio.h>
#include <stdlib.h>

struct profile{
    char name[18];
    int age;
    float height;
};

int main(){
    FILE *fp;
    struct profile list[] = {
        {"Takako Toyota", 25, 163.42},
        {"Mizuho Kagami", 21, 155.89},
        {"Yoshie Tanaka", 25, 168.23},
        {"Mai Nobe", 22, 145.89}
    };

    if((fp=fopen("list_binary.bin", "wb")) == NULL){
        perror("list_binary.bin");
        exit(EXIT_FAILURE);
    }

    fwrite(list, sizeof(struct profile), 4, fp);

    if(fclose(fp) == EOF){
        perror("list_binary.bin");
        exit(EXIT_FAILURE);
    }
}