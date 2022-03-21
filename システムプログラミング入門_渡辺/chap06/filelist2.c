#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>

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
        struct stat st;
        if(lstat(ent->d_name, &st) < 0){
            perror(ent->d_name);
            exit(EXIT_FAILURE);
        }

        int is_IFLNK = (st.st_mode & S_IFLNK);
        int is_IFDIR = (st.st_mode & S_IFDIR);


        printf("%s%s\t\n", ent->d_name, is_IFDIR ? "/" : is_IFLNK ? "@" : "");

    }

    closedir(directory);


}