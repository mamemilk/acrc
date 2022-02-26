#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

#define BUFSIZE 512
#define LISTNUM 20

typedef struct profile{
    char name[24];
    int age;
} profile;

profile profile_list[LISTNUM];

int main(int argc, char *argv[]){
    FILE *fpin;
    char buf[BUFSIZE];

    if(argc != 2){
        fprintf(stderr, "Usage : copy <source> <destination>\n");
        exit(EXIT_FAILURE);
    }

    if((fpin=fopen(argv[1], "r")) == NULL){
        perror(argv[1]);
        exit(EXIT_FAILURE);
    }

    //1行1レコードを前提に書く。
    int index = 0;
    while(fgets(buf, BUFSIZE-1, fpin) != NULL){
        int i = 0;
        profile p;
        while(buf[i] != ','){
            p.name[i] = buf[i];
            i++;
        }
        i++;

        long val;
        char *endptr;
        val = strtol(buf+i, &endptr, 10);
        p.age = (int)val;
        
        profile_list[index] = p;
        index++;
    }

    for(int i=0;i<index;i++){
        printf("[NO.%d]\n", i);
        printf("  name=%s\n",profile_list[i].name);
        printf("  age=%d\n",profile_list[i].age);
    }

    if(EOF == fclose(fpin)){
        perror(argv[1]);
        exit(EXIT_FAILURE);
    }
}