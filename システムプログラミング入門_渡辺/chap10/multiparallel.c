#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>

int main(){
    const int mul_num = 2;
    pid_t ret[mul_num];
    int p;
    int i;

    printf("[BEFORE FORK]\n Process ID : %d\t Parent Process ID : %d\n", getpid(), getppid());
    for(p=0;p<mul_num && (ret[p] = fork()) > 0;p++);

    srand(time(NULL));
    printf("[AFTER FORK]\n Process ID : %d\t Parent Process ID : %d\n", getpid(), getppid());
    for(i=0;i<mul_num;i++){
        printf("[id=%d] Return Value of Fork : %d\n", getpid(), ret[i]);
    }
    printf("\n");

    sleep(1);
    for(i = 0;i < 5; i++){
        printf("(%d) for loop i=%d\n", getpid(), i);
    }

    if(p < mul_num){
        printf("(%d) End the child process\n", getpid());
    }else if (p == mul_num){
        printf("(%d) End the parent process\n", getpid());
    }else{
        perror("ERROR");
        exit(EXIT_FAILURE);
    }

}