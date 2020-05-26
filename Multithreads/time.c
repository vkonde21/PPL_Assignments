#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include <time.h> 
#include<unistd.h> //for sleep function
int hour;
int minute;
int second;
pthread_mutex_t m;  //mutex type
pthread_t thread1;
pthread_t thread2;
pthread_t thread3;

void *hours(){
	while(1){
		if (minute == 60)
		{
			if (hour == 23)
			{
				hour = 0;
			}
			else{
			hour = hour + 1;
		}
		minute = 0;
		second = 0;
	}
	}
}

void *minutes(){
	while(1){
		if (second == 60)
		{
			minute = minute + 1;
			second = 0;
			
		}
	}
}


void *seconds(){
	while(1){
		pthread_mutex_lock(&m);
		second = second + 1;
		sleep(1);
		pthread_mutex_unlock(&m);
	}
}
	


int main(int argc, char *argv[]){
	time_t s, val = 1; 
    struct tm* current_time;
	//If you pass in NULL, it just ignores it and merely returns a new time_t object that represents the current time.
	//The call to time(NULL) returns the current calendar time (seconds since Jan 1, 1970).
	s = time(NULL); 
    current_time = localtime(&s); 
    //The localtime() function return the local time of the user i.e time present at the task bar in computer.
  	int hr = current_time->tm_hour;
  	int min = current_time->tm_min;
  	int sec = current_time->tm_sec;
  	int value = 4;
	int err1,err2,err3;
	hour = hr;
	minute = min;
	second = sec;
	
	
	err1 = pthread_mutex_init(&m, NULL);
	if(err1 != 0){
		printf("Mutex initialization failed!!!");
	}

	err1 = pthread_create(&thread1, NULL, seconds, NULL);
	err2 = pthread_create(&thread2, NULL, minutes, NULL);
	err3 = pthread_create(&thread3, NULL, hours, NULL);
	if(err1 || err2 || err3){
		printf("Thread initialization failed");
		return 0;
	}

	
	while(1){
		printf("\r%02d: %02d: %02d", hour, minute, second);
	}
	pthread_mutex_destroy(&m);
	return 0;
}

/*
int pthread_mutex_lock(pthread_mutex_t *mutex); //locks calling thread if mutex is in use
int pthread_mutex_unlock(pthread_mutex_t *mutex);
code written between these 2 blocks is considered as critical section

int pthread_mutex_init(pthread_mutex_t *mutex, const pthread_mutexattr_t *attr)
mutex attributes == specifies mutex behavior when a mutex is shared among processes
*/
