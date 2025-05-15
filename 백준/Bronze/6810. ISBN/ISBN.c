#include <stdio.h>
#include <math.h>

#define LENGTH 13

int main(void) {
	char base[LENGTH] = "9780921418";
	int multiply[]={1,3};
	char a,b,c;
	int sum=0;
	
	scanf("%c %c %c",&a,&b,&c);
	
	base[10] = a;
	base[11] = b;
	base[12] = c;

	for (int i = 0; i < LENGTH; i++) {
		sum+=(base[i]-'0')*multiply[i%2];
	}

	printf("The 1-3-sum is %d",sum);
	return 0;
}