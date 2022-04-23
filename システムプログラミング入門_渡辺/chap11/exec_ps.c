#include <stdio.h>
#include <unistd.h>
//#include <stdlib.h>

int main(){
    printf("Exec ps program...\n");
    execlp("ps", "ps", "-l", NULL);
    printf("done.\n"); //this line is not reached
}