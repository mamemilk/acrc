#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[]){
    if(argc != 2){
        fprintf(stderr, "Usage : %s <filename>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    char renamed[256+1];
    char trash_path[] = "./trash_dir/";
    sprintf(renamed, "%s%s", trash_path, argv[1]);

    if(rename(argv[1], renamed) < 0){
        perror(argv[1]);
        exit(EXIT_FAILURE);
    }

}