#include <stdio.h>
#include <ctype.h>

enum {INT = 1, FLOAT, ID, NUM, REAL, COMMA, EQ, EX, QU, SEMI, ADD, SUB, MUL, DIV, LPAR, RPAR, ERROR};

int status2token[] = {
    0,      //0
    0,      //1
    ID,     //2
    ID,     //3
    ID,     //4
    ID,     //5
    FLOAT,  //6
    ID,     //7
    ID,     //8
    ID,     //9
    INT,    //10
    NUM,    //11
    0,      //12
    REAL,   //13
    NUM,    //14
    0,      //15
    DIV,    //16
    0,      //17
    0,      //18
    0,      //19
    0,      //20
    ADD,    //21
};


//char *yytext;
char yytext[1024];

int yylex(){
    char c;

    int status = 1;
    int LF = 0;
    int posLF = 0;
    int ptr=0;

    while(1){
        // statusが0になったら、字句の区切り
        if (status == 0) {
            if (LF != 0) {
                if ((status = status2token[LF]) > 0) {
                    return status;
                }
                status = 1;
                LF = 0;
                posLF = 0;
                ptr = 0;
            } else {
                printf("ERROR : \n");
                return 0;
            }
        }

        if((c = getc(stdin)) == EOF ) break;
        yytext[ptr++] = c;

        switch(status){
            case 1:
                if (c == 'f') {
                    status = LF = 2;
                    posLF = ptr;
                }
                else if (c == 'i') {
                    status = LF = 8;
                    posLF = ptr;
                }
                else if (isalpha(c)) {
                    status = LF = 7;
                    posLF = ptr;
                }
                else {
                    status = 0;
                }
                break;
            case 2:
                if (c == 'l') {
                    status = LF = 3;
                    posLF = ptr;
                } else if (isalnum(c)) {
                    status = LF = 7;
                    posLF = ptr;
                } else {
                    status = 0;
                }
                break;
            case 7:
                if (isalnum(c)) {
                    status = LF = 7;
                    posLF = ptr;
                } else {
                    status = 0;
                }
                break;
            case 8:
                if (c == 'n') {
                    status = LF = 9;
                    posLF = ptr;
                } else if (isalnum(c)) {
                    status = LF = 7;
                    posLF = ptr;
                } else {
                    status = 0;
                }
                break;
        }

        printf("%c status : %d, LF : %d, posLF : %d\n", c, status, LF, posLF);

    }
    return 0;
}

int yywrap(void){return 1;}
int main(void){
    int t;
    while((t=yylex()) != 0){
        printf("number = %d, string '%s'\n", t, yytext);
    }
}
