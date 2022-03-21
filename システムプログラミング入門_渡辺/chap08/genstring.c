#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char* gen_string();

int main(){
    char *str;
    //u_int64_t addr;

    str = gen_string();

    printf("----- variables(main) ------\n");
    printf("str          :%16lx\n", str);
    printf("----- functions(main) ------\n");
    printf("gen_string   :%16lx\n", gen_string);
    printf("printf       :%16lx\n", printf);
    printf("getchar      :%16lx\n", getchar);
    printf("main         :%16lx\n", main);

    /* step 2 */
    printf("input any key\n");
    //scanf("%x", &addr);
    getchar();
    printf("generated string\t%s\n", str);
    //printf("generated string at %x\t%s\n", addr, (char *)addr);

}

char* gen_string(){
    char array[8];
    int i;
    srand(time(NULL));
    for(i=0;i<8;i++){
        array[i] = rand() % ('z' - 'A') + 'A';
    }

    printf("----- variables(gen_string) ------\n");
    printf("array        :%16lx\n", array);
    printf("i            :%16lx\n", &i);
    
    printf("----- functions(gen_string) ------\n");
    printf("gen_string   :%16lx\n", gen_string);

    /* step 1 */
    return array;
}