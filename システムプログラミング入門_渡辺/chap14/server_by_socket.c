#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <stdlib.h>
#include <unistd.h>

#include <string.h>

#define BUFFER_SIZE 256

int main(int argc, char *argv[])
{
    unsigned short port;
    int srcSocket;
    int dstSocket;

    struct sockaddr_in srcAddr;
    struct sockaddr_in dstAddr;

    int dstAddrSize = sizeof(dstAddr);

    int numrcv;
    char buffer[BUFFER_SIZE];

    srcSocket = socket(PF_INET, SOCK_STREAM, 0);

    port = (unsigned short) atoi(argv[1]);
    
    memset(&srcAddr, 0, sizeof(srcAddr));
    srcAddr.sin_port = htons(port);
    srcAddr.sin_family = PF_INET;
    srcAddr.sin_addr.s_addr = htonl(INADDR_ANY);
    printf("Address = %s, Port = %u\n", inet_ntoa(srcAddr.sin_addr), port);
    bind(srcSocket, (struct sockaddr *) &srcAddr, sizeof(srcAddr));

    listen(srcSocket, 1);

    printf("waigint\n");
    dstSocket = accept(srcSocket, (struct sockaddr *)&dstAddr, &dstAddrSize);

    printf("connected from %s\n", inet_ntoa(dstAddr.sin_addr));

    while(1){
        memset(buffer, 0 , BUFFER_SIZE);
        numrcv = recv(dstSocket, buffer, BUFFER_SIZE, 0);
        if (numrcv == 0 || numrcv == -1){
            int status = close(dstSocket); 
            break;
        }
        printf("recieved : %s\n", buffer);
        send(dstSocket, buffer, numrcv, 0);
        if(strncmp(buffer, "quit", 4) == 0) break;
    }
}
