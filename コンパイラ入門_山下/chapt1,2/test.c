#include <stdio.h>

int main(void){
  int i;
  float sum = 0;
  for(i=0; i<=10; i++){
    sum += i;
    printf("%f\n",sum);
  }
}
