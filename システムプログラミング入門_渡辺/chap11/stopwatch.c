#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

//https://www.mm2d.net/main/prog/c/time-05.html

struct timespec ts;
struct timespec ts_stop;

void stop(){
    clock_gettime(CLOCK_REALTIME, &ts_stop);
    //printf("time:    %10ld.%09ld CLOCK_REALTIME\n", ts_stop.tv_sec, ts_stop.tv_nsec);

    printf("TIME: %ld seconds", ts_stop.tv_sec - ts.tv_sec);

    printf("[r] restart, [q] quit\t");
    char ans = getchar();
    while(getchar() != '\n'){}

    if(ans == 'r'){
        clock_gettime(CLOCK_REALTIME, &ts);
    }else{
        exit(EXIT_SUCCESS);
    }
}

int main(){

    signal(SIGINT, stop);

    //printf("time():  %10ld\n", time(NULL));
    clock_getres(CLOCK_REALTIME, &ts);
    //printf("res :    %10ld.%09ld CLOCK_REALTIME\n", ts.tv_sec, ts.tv_nsec);
        
    clock_gettime(CLOCK_REALTIME, &ts);
    //printf("time:    %10ld.%09ld CLOCK_REALTIME\n", ts.tv_sec, ts.tv_nsec);

    while(1){

    }
    
    return 0;
}