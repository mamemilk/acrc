#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
//#include <sys/sem.h>
#include <time.h>

int main (int argc, char *argv[]){
    int id,tmp;//,sid,i;
    int *A, *B;
    int num;
    //union semun inival;
    //struct sembuf semlock;
    struct shmid_ds buf;

    //semlock.sem_num = 0;
    //semlock.sem_flg = 0;

    srand((unsigned)time(NULL));


    if(argc == 1){
        if((id=shmget(IPC_PRIVATE, sizeof(int), IPC_CREAT|0666)) == -1){
            perror("shmget");
            exit(EXIT_FAILURE);
        }
        // if ((sid = semget(id, 1, IPC_CREAT|0700)) == -1){
        //     perror("semget");
        //     exit(EXIT_FAILURE);
        // }
        // inival.val = 1;
        // semctl(sid, 0, SETVAL, inival);
        printf("shared memory ID = %d\n", id);
    }else if(argc==2){
        id = atoi(argv[1]);
        // if((sid = semget(id,1,0)) == -1){
        //     perror("semget");
        //     exit(EXIT_FAILURE);
        // }
    }

    A = (int *)shmat(id, 0, 0);
    B = A + 1;
    *A = 100;
    *B = 0;

    sleep(5);
    while (*A > 0) {
        int tmp = *A;
        tmp--;
        *A = tmp;

        sleep(rand() % 10);

        tmp = *B;
        tmp++;
        *B = tmp;

        printf("%d\n", *A + *B);
        sleep(rand() % 4);
    }

    shmctl(id, IPC_STAT, &buf);


    if (shmdt(A) == -1){perror("shmdt");}

    if (buf.shm_nattch == 1) {
        if (shmctl(id, IPC_RMID, 0) == -1) perror("shmctl");
    }

    //if(semctl(sid, IPC_RMID, 0) == -1){perror("semctl");}

}
