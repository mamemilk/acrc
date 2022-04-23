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
    argv[0] = "finger";
    while(1){
        printf("fingersh[%d]>", cnt++);
        if(fgets(str,BUFSIZE,stdin) == NULL){
            perror(str);
            exit(EXIT_FAILURE);
        }
        chop (str);
        int argc = argsplit(str, argv+1);
        //printf("%d\n", argc);
        if(strcmp(argv[1], "quit") == 0 || strcmp(argv[1], "exit") == 0){
            break;
        }
        ret = fork();

        if(ret == 0){
            //if(argc!=0){
            execvp(argv[0], argv);
            //}
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
    return argc;
}
void chop(char *str){
    str[strlen(str)-1] = '\0';
}
