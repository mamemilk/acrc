#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
    pid_t pid;
    int status;

    printf("Exec ps program...\n");
    pid = fork();
    if(pid == 0){
        execlp("ps", "ps", "-l", NULL);
    }else if(pid > 0){
        wait(&status);
        printf("done. \n");
    }else{
        perror("fork");
        exit(EXIT_FAILURE);
    }
}