#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>


void chop(char *);

int main()
{
    char str[256];
    int fd[2];
    pid_t ret;
    int status;

    long val;
    char *endptr;

    if (pipe(fd) < 0) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    ret = fork();

    if (ret == 0) {
        read(fd[0], val, sizeof(val));
        printf("A child process: My parent said, %ld*%ld = %ld\n", val, val, val*val);
        val = val*val;
        write(fd[1], &val, sizeof(val));
    }
    else if (ret == -1) {
        perror("fork");
        exit(1);
    }
    else {
        printf("A parent process: input number>");
        fgets(str, sizeof(str), stdin);
        chop(str);
        val = strtol(str, &endptr, 10);
        printf("parent > %ld", val);
        write(fd[1], &val, sizeof(val));
        wait(&status);
        read(fd[0], &val, sizeof(val));
        printf("A parent process: answer = %ld\n", val);
     }
}        

void chop(char *str)
{
    str[strlen(str)-1] = '\0';
    return;
}
