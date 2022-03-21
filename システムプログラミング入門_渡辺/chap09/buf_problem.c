#include <stdio.h>

void func(){
    char buf[256+1];
    char c;
    int i=0;
    while((c=getchar()) != EOF && i < 256){
        buf[i] = c;
        i++;
    }
    buf[i] = '\0';
    printf("buf=%s\n", buf);
}

int main(){
    func();
}