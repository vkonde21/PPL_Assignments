#include<stdio.h>
int fact(int n){
	if(n == 0 || n == 1){
		return 1;
	}
	return n * fact(n - 1);
}

int main(){
	int a = fact(3);
	return 0;
}
