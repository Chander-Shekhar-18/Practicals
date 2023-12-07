#include <stdio.h>
#include <stdlib.h> 
#include <string.h> 
#include <sys/ipc.h> 
#include <sys/shm.h> 
#include <unistd.h>

#define SHM_KEY 1024
#define SHM_SIZE 128

int main()
{
    int shmid;
    char
        *shared_memory = NULL;

    shmid = shmget(SHM_KEY, SHM_SIZE, 0666);
    if (shmid < 0)
    {
        printf("Some error occurred !!! \n");
        return 1;
    }

    shared_memory = (char *)shmat(shmid, NULL, 0);
    if ((void *)shared_memory == (void *)-1)
    {
        printf("Some error occurred !!! \n");
        return 1;
    }

    while (1)
    {
        while (shared_memory[0] != '1')
        {
            sleep(1);
        }

        printf("Message received from Client: %s\n", (shared_memory + 1));

        printf("Enter a message for the Client : ");
        fgets(shared_memory + 1, SHM_SIZE - 1, stdin);
        shared_memory[0] = '1';
        shared_memory[strcspn(shared_memory + 1, "\n") + 1] = '\0';

        if (strcmp(shared_memory + 1, "STOP") == 0)
        {
            printf("Communication Break !!! \n");
            break;
        }
        else
            shared_memory[0] = '\0';

        while (shared_memory[0] != '1')
        {
            sleep(1);
        }

        if (strcmp(shared_memory + 1, "STOP") == 0)
        {
            printf("Communication Break !!! \n");
            break;
        }

        printf("Enter a message for the Client : ");
        fgets(shared_memory + 1, SHM_SIZE - 1, stdin);
        shared_memory[0] = '1';
        shared_memory[strcspn(shared_memory + 1, "\n") + 1] = '\0';

        if (strcmp(shared_memory + 1, "STOP") == 0)
        {
            printf("Communication Break !!! \n");
            break;
        }

        // printf("Server sent this message: %s\n", (shared_memory + 1));

        shared_memory[0] = '\0';
    }

    shmdt(shared_memory);
    return 0;
}