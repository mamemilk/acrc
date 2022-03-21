#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <mntent.h>

int main(int argc, char* argv[]){
    long mntsize;
    struct mntent *mntbuf;

    int i;

    mntsize = getmntinfo(&mntbuf, MNT_WAIT);
    printf("\n");
    printf("Filesystem 512-block\n");
    for(i=0; i<mntsize; i++){
        printf("%27s\t%ld\n", mntbuf[i].f_mntfromname, mntbuf[i].f_blocks);
    }
    printf("\n");
}