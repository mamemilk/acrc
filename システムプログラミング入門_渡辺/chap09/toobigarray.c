#include <stdio.h>

int main(){
    int a[1500000];
    int b[1000000];
    int c = 0;
    printf("&a=%lx, &b=%lx, &c=%lx\n", a, b, &c);
}