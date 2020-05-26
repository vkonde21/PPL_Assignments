#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

pthread_t hello;
pthread_t goodbye;
pthread_mutex_t lock;

void *printfunc(void *vargp)
{
    while (1)
    {
        pthread_mutex_lock(&lock);
        printf("%s\n", (char *)vargp);
        pthread_mutex_unlock(&lock);
        sleep(1);
    }
}

int main()
{
    char s[20] = "Hello World";
    char g[20] = "Goodbye World";
    if (pthread_mutex_init(&lock, NULL) != 0)
    {
        printf("Mutex initialization failed.\n");
        return 0;
    }
    
    int err1 = pthread_create(&hello, NULL, &printfunc, &s);
    int err2 = pthread_create(&goodbye, NULL, &printfunc, &g);
    
    if (err1 != 0 || err2!=0)
    {
        printf("Thread initialization failed\n");
        return 0;
    }

    pthread_join(hello, NULL);
    pthread_join(goodbye, NULL);
    pthread_mutex_destroy(&lock);
    pthread_exit(NULL);
    return 0;
}