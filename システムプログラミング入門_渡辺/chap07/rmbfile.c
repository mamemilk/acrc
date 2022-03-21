#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>

#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[]){
    DIR *directory;
    struct dirent *ent;


    if(argc != 2){
        fprintf(stderr, "Usage : %s <filename>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    directory = opendir(argv[1]);
    if (!directory){
        perror(argv[1]);
        exit(EXIT_FAILURE);
    }

    while((ent = readdir(directory)) != NULL){
        if(ent->d_name[strnlen(ent->d_name, 256)-1] == '~'){
            char ans[20];
            printf("\tDo you remove the file %s ?[y/n/q]", ent->d_name);
            scanf("%s", ans);
            if(ans[0] == 'y'){
                if(unlink(ent->d_name) < 0){
                    perror(ent->d_name);
                    exit(EXIT_FAILURE);
                }
            }else if(ans[0] == 'n'){
                continue;
            }else if(ans[0] == 'q'){
                break;
            }else{
                continue;  
            }
        }
    }

    closedir(directory);


}