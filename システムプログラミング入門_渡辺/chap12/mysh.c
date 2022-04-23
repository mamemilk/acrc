#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#define BUFSIZE 512

int argsplit(char *str, char *argv[]);
void chop(char *str);

int main(){
    pid_t ret;
    int status, cnt = 0;
    char str[BUFSIZE];
    char *argv[20];
    while(1){
        printf("mysh[%d]>", cnt++);
        if(fgets(str,BUFSIZE,stdin) == NULL){
            perror(str);
            exit(EXIT_FAILURE);
        }
        chop (str);
        argsplit(str, argv);
        if(strcmp(argv[0], "quit") == 0){
            break;
        }
        ret = fork();

        if(ret == 0){
            execvp(argv[0], argv);
        }else if(ret > 0){
            wait(&status);
        }else{
            perror("fork");
            exit(EXIT_FAILURE);
        }

    }
}


int argsplit(char *str, char *argv[]){
    int i = 0;
    int is_met = 0;
    int argc = 0;
    while(str[i] != '\0'){
        if(str[i]==' '){
            str[i] = '\0';
            is_met = 0;
        }else if(is_met == 0){
            is_met = 1;
            argv[argc++] = str+i;
        }
        i++;
    }
    argv[argc] = NULL;
}
void chop(char *str){
    str[strlen(str)-1] = '\0';
}
