#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char *argv[]){
    struct stat st;

    if(argc != 2){
        fprintf(stderr, "Usage : %s <filename>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    if(lstat(argv[1], &st) < 0){
        perror(argv[1]);
        exit(EXIT_FAILURE);
    }

    int user_rights = (st.st_mode >> 6 ) & 0x7;
    int group_rights = (st.st_mode >> 3 ) & 0x7;
    int others_rights = (st.st_mode >> 0 ) & 0x7;

    printf("For user : %s %s %s\n", user_rights & 0x4 ? "read" : "", 
                                    user_rights & 0x2 ? "write" : "", 
                                    user_rights & 0x1 ? "execute" : "");

    printf("For group : %s %s %s\n", group_rights & 0x4 ? "read" : "", 
                                     group_rights & 0x2 ? "write" : "", 
                                     group_rights & 0x1 ? "execute" : "");

    printf("For others : %s %s %s\n", others_rights & 0x4 ? "read" : "", 
                                      others_rights & 0x2 ? "write" : "", 
                                      others_rights & 0x1 ? "execute" : "");
}