/*
  strtol関数で書き直す
  エラー処理を実装する(一文字でも10進数でないものが含まれてたらエラー出力して終了するようにする。) 


*/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <errno.h>

int mystrtol_base10(char *str, long *valptr){
    long val;
    char *endptr;
    errno = 0;    /* To distinguish success/failure after call */
    
    val = strtol(str, &endptr, 10);

    /* Check for various possible errors */
    if ( errno != 0 )
    {
        perror("strtol");
        exit(EXIT_FAILURE);
    }

    if (endptr == str)
    {
        fprintf(stderr, "No digits were found\n");
        exit(EXIT_FAILURE);
    }

    /* If we got here, strtol() successfully parsed a number */
    //printf("strtol() returned %ld\n", val);

    if (*endptr != '\0') {/* Not necessarily an error... */
        fprintf(stderr, "Further characters after number: %s\n", endptr);
        exit(EXIT_FAILURE);
    }

    *valptr = val;

    //exit(EXIT_SUCCESS);
    return 0;
}


int main(int argc, char *argv[])
{
    long a, b, c;
    char *endptr_a, *endptr_b;

    if (argc != 3)
    {
        fprintf(stderr, "Usage: %s <num> <num>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    mystrtol_base10(argv[1], &a);
    mystrtol_base10(argv[2], &b);

    c = a + b;
    printf("%lu + %lu = %lu\n", a, b, c);
}
