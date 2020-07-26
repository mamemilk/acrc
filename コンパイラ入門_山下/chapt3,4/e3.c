#include <stdio.h>
#include <ctype.h>

enum {INT = 1, FLOAT, ID, NUM, REAL, COMMA, EQ, EX, QU, SEMI, ADD, SUB, MUL, DIV, LPAR, RPAR, ERROR};

int state2token[] = {
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

    int state = 1;
    int LF = 0;
    int posLF = 0;
    int ptr=0;

    while(1){
        // stateが0になったら、字句の区切り
        if (state == 0) {
            if (LF != 0) {
                while(ptr > posLF){
                    ungetc(yytext[--ptr], stdin);
                }
                yytext[ptr] = 0;

                if ((state = state2token[LF]) > 0) {
                    return state;
                }
                state = 1;
                LF = 0;
                posLF = 0;
                ptr = 0;

            }else {
                printf("ERROR : \n");
                return 0;
            }
        }

        if((c = getc(stdin)) == EOF ) break;
        yytext[ptr++] = c;

        switch(state){
            case 1:
                if (c == 'f') {
                    state = LF = 2;
                    posLF = ptr;
                }else if (c == 'i') {
                    state = LF = 8;
                    posLF = ptr;
                }else if (isalpha(c)) {
                    state = LF = 7;
                    posLF = ptr;
                }else if (c == '0') {
                    state = LF = 11;
                    posLF = ptr;
                }else if (isdigit(c)) {
                    state = LF = 14;
                    posLF = ptr;
                }else if (c == '.') {
                    state = 15;//state = LF = 15;
                    posLF = ptr;
                }else if (c == '/') {
                    state = LF = 16;
                    posLF = ptr;
                }else if (c == '\n' || c == '\t' || c == ' ') {
                    state = LF = 20;
                    posLF = ptr;
                }else if (c == '+') {
                    state = LF = 21;
                    posLF = ptr;
                }
                else {
                    state = 0;
                }
                break;
            case 2:
                if (c == 'l') {
                    state = LF = 3;
                    posLF = ptr;
                }else if (isalnum(c)) {
                    state = LF = 7;
                    posLF = ptr;
                }else {
                    state = 0;
                }
                break;
            case 7:
                if (isalnum(c)) {
                    state = LF = 7;
                    posLF = ptr;
                }else {
                    state = 0;
                }
                break;
            case 8:
                if (c == 'n') {
                    state = LF = 9;
                    posLF = ptr;
                }else if (isalnum(c)) {
                    state = LF = 7;
                    posLF = ptr;
                }else {
                    state = 0;
                }
                break;
            case 9:
                if (c == 't') {
                    state = LF = 10;
                    posLF = ptr;
                }else if (isalnum(c)) {
                    state = LF = 7;
                    posLF = ptr;
                }else {
                    state = 0;
                }
                break;
            case 10:
                if (isalnum(c)) {
                    state = LF = 7;
                    posLF = ptr;
                }else {
                    state = 0;
                }
                break;
            case 11:
                if (isdigit(c)) {
                    state = 12;//state = LF = 12;
                    //posLF = ptr;
                }else {
                    state = 0;
                }
                break;
            case 12:
                if (isdigit(c)) {
                    state = 12;//state = LF = 12;
                    //posLF = ptr;
                }else if (c == '.') {
                    state = LF = 13;
                    posLF = ptr;
                }else {
                    state = 0;
                }
                break;
            case 13:
                if (isdigit(c)) {
                    state = LF = 13;
                    posLF = ptr;
                }else {
                    state = 0;
                }
                break;
            case 14:
                if (isdigit(c)) {
                    state = LF = 14;
                    posLF = ptr;
                }else if (c == '.') {
                    state = LF = 13;
                    posLF = ptr;
                }else {
                    state = 0;
                }
                break;
            case 15:
                if (isdigit(c)) {
                    state = LF = 13;
                    posLF = ptr;
                }else {
                    state = 0;
                }
                break;
            case 16:
                if (c == '*') {
                    state = 17;//state = LF = 17;
                    //posLF = ptr;
                }else {
                    state = 0;
                }
                break;
            case 17:
                if (isalnum(c) || c == ' ') {
                    state = 17;//state = LF = 17;
                    //posLF = ptr;
                }else if (c == '*') {
                    state = 18;//state = LF = 18;
                    //posLF = ptr;
                }else {
                    state = 0;
                }
                break;
            case 18:
                if (c == '/') {
                    state = LF = 19;
                    posLF = ptr;
                }else {
                    state = 0;
                }
                break;
            case 19:
                state = 0;
                break;
            case 20:
                state = 0;
                break;
            case 21:
                state = 0;
                break;
        }

        printf("%c %d state : %d, LF : %d, posLF : %d\n", c, ptr, state, LF, posLF);

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
