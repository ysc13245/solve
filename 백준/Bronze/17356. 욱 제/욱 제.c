#include <stdio.h>
#include <math.h>

int main(void) {
	int a, b;
	scanf("%d %d", &a, &b);
	double m=(b-a)/400.0;

	printf("%f", 1.0/(1.0+pow(10.0,m)));
	
	return 0;
}