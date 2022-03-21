#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char* gen_string();
char* gen_string2();

int main(){
    char *str;
    char *str2;

    str = gen_string();
    str2 = gen_string2();

    /* step 2 */
    printf("input any key\n");
    getchar();
    printf("generated string\t%s\n", str);
    printf("generated string\t%s\n", str2);
    free(str2);
}

char* gen_string(){
    char array[8];
    int i;
    srand(time(NULL));
    for(i=0;i<8;i++){
        array[i] = rand() % ('z' - 'A') + 'A';
    }

    /* step 1 */
    return array;
}

char* gen_string2(){
    char *array;
    array = (char*)malloc(sizeof(char)*8);
    int i;
    srand(time(NULL));
    for(i=0;i<8;i++){
        array[i] = rand() % ('z' - 'A') + 'A';
    }

    /* step 1 */
    return array;
}