#include<stdio.h>
int main(){
	int a,b;
	scanf("%d %d",&a,&b);
	int sub = b-a;
	if (sub>30){
		printf("You are speeding and your fine is $500.");
	}else if (sub>20){
		printf("You are speeding and your fine is $270.");
	}else if (sub>0){
		printf("You are speeding and your fine is $100.");
	}else{
		printf("Congratulations, you are within the speed limit!");
	}

	return 0;
}