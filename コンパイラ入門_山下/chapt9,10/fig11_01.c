int main(int argc, char *argv[]) {
    if(argc > 1) {
            yyin = fopen(argv[1], "r");
        if(!yyin){
            fprintf(stderr,"fopen error_n"); 
            exit(1); 
        }
    }else {
        fprintf(stderr,"arg error_n"); 
        exit(1);
    }
    if(!yyparse()){
        ...
    }
}
