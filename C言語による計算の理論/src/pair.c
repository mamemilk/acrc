#include <stdlib.h>
#include <stdio.h>

int pair(int x, int y){
    return (x+y)*(x+y+1)/2 + x + 1;
}

int left(int z){
    int x,y;

    if(z==0){
        return(0);
    }

    x = 0;
    while (x<z){
        y = 0;
        while (y<z){
            if (pair(x,y) == z){
                return(x);
            }
            y++;
        }
        x++;
    }
}

int right(int z){
    int x,y;

    if(z==0){
        return(0);
    }

    x = 0;
    while (x<z){
        y = 0;
        while (y<z){
            if (pair(x,y) == z){
                return(y);
            }
            y++;
        }
        x++;
    }
}

int element(int a, int i){
    int l = left(a);
    int r = right(a);
    
    int loop = 1;

    while(1){
        if(loop==i){
            return(l);
        }

        l = left(r);
        r = right(r);
        loop++;
    }
}

int length(int a){
    int l = left(a);
    int r = right(a);

    int loop = 1;

    while(1){
        if(r==0){
            return(loop);
        }

        l = left(r);
        r = right(r);
        loop++;
    }
}

int sequence(int x, int k){
    int p = pair(x,0);

    int loop = 1;

    while(1){
        if(loop==k){
            return(p);
        }
        p = pair(x,p);
        loop++;
    }
}

int replace(int a, int i, int x){
    int b, j;

    b = 0;
    j = length(a);
    while(j>0){
        if(j==i)
          b = pair(x,b);
        else
          b = pair(element(a,j),b);
        
        j--;
    }
    return(b);
}

int is_code(int p){
    int pc, v, i, k, m, n, S, a, b;

    //int num_inputs = left(n); //p[1]
    //int num_variables = left(right(n)); //p[2]
    //int num_code = right(right(n)); //p[3]
    k = element(p,1);
    m = element(p,2);
    S = element(p,3);
    n = length(S) + 1;

    pc = 1;

    while(pc < n){
        if(element(S, pc)==1){
            pc++;
        }else if(element(S, pc)==2){
            pc++;
            pc++;
        }else if(element(S, pc)==3){
            pc++;
            pc++;
        }else if(element(S, pc)==4){
            pc++;
        }else if(element(S, pc)==5){
            pc++;
        }else if(element(S, pc)==6){
            pc++;
            pc++;
        }else{
            return 0;
        }
    }
    return 1;
}


int is_executable(int p, int x){
    int pc, v, i, k, m, n, S, a, b;

    k = element(p,1);
    m = element(p,2);
    S = element(p,3);
    n = length(S) + 1;

    if(k == length(x) && is_code(p)){
        return 1;
    }else{
        return 0;
    }
}

int main(){
    printf("%d\n", pair(10,pair(5,pair(0,pair(2,0)))));

    printf("%d\n", left (77826));
    printf("%d\n", right(77826));

    printf("element : %d\n", element(77826,1));
    printf("element : %d\n", element(77826,2));
    printf("element : %d\n", element(77826,3));
    printf("element : %d\n", element(77826,4));
    printf("element : %d\n", element(77826,5));
    printf("element : %d\n", element(77826,6));

    printf("length  : %d\n", length(77826));

    printf("pair    : %d\n", pair(1,pair(1,pair(1,0))));
    printf("pair    : %d\n", sequence(1,3));

    //桁あふれする。
    printf("tashizam    is %d\n", pair(2,pair(2, 
                                              pair(pair(6,pair(2,3)),
                                                   pair( pair(1,6),
                                                         pair( pair(5,2), 
                                                               pair( pair(4,1),
                                                                     pair( pair(1,1), 0))))))));

    printf("example code is %d\n", pair(2, 
                                        pair(2, 
                                             pair(6, pair(2, 3)))));

    int s0 = pair(2,3);
    int s1 = pair(6, s0);
    int s2 = pair(2, s1);
    int s3 = pair(2, s2);

    printf("%d %d %d %d\n", s0, s1, s2, s3);

    printf("is_code(16) : %d\n", is_code(16));
    return 0;
}