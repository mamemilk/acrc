#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/sem.h>
#include <time.h>

// 自分で定義しないといけない．えええ．
//https://ribf.riken.jp/~baba/tips/semun.html
#if defined(__GNU_LIBRARY__) && !defined(_SEM_SEMUN_UNDEFINED)
/* 共用体 semun の定義は <sys/sem.h> に含まれている */
#else
/* X/OPEN に従うならば自分自身で以下のように定義しなければならない */
union semun {
     int val;                    /* value for SETVAL */
     struct semid_ds *buf;       /* buffer for IPC_STAT, IPC_SET */
     unsigned short int *array;  /* array for GETALL, SETALL */
     struct seminfo *__buf;      /* buffer for IPC_INFO */
};
#endif

int main(int argc, char *argv[]){
    int id,tmp,sid,i;
    int *counter;
    int num;
    union semun inival;
    struct sembuf semlock;
    struct shmid_ds buf;

    semlock.sem_num = 0;
    semlock.sem_flg = 0;
    srand((unsigned) time(NULL));

    if(argc == 1){
        if((id=shmget(IPC_PRIVATE, sizeof(int), IPC_CREAT|0666)) == -1){
            perror("shmget");
            exit(EXIT_FAILURE);
        }
        if ((sid = semget(id, 1, IPC_CREAT|0700)) == -1){
            perror("semget");
            exit(EXIT_FAILURE);
        }
        inival.val = 1;
        semctl(sid, 0, SETVAL, inival);
        printf("shared memory ID = %d\n", id);
    }else if(argc==2){
        id = atoi(argv[1]);
        if((sid = semget(id,1,0)) == -1){
            perror("semget");
            exit(EXIT_FAILURE);
        }
    }
    printf("Input the number to add > ");
    scanf("%d", &num);

    counter = (int *)shmat (id, 0, 0);
    if(argc == 1){
        *counter = 0;
    }

    for(int i=0;i<3;i++){
        semlock.sem_num = 0;
        semlock.sem_op = -1;
        semlock.sem_flg = 0;
        if(semop(sid, &semlock, 1) < 0){break;}
        tmp =* counter;
        fprintf(stderr, "counter=%d", tmp);
        sleep(rand()%4);
        tmp += num; 
        *counter = tmp;

        semlock.sem_num = 0;
        semlock.sem_op = 1;
        semlock.sem_flg = 0;

        if(semop(sid, &semlock, 1) < 0){break;}

        fprintf(stderr, " -> %d\n", *counter);
        sleep(rand() % 4);
    }

    shmctl(id, IPC_STAT, &buf);


    if(shmdt (counter) == -1) {perror("shmdt");}

    if(buf.shm_nattch == 1){
        if(shmctl(id, IPC_RMID, 0) == -1){perror("chmctl");}
    }

    if(semctl(sid, IPC_RMID, 0) == -1){perror("semctl");}

}