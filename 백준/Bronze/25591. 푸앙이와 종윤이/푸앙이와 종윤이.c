#include <stdio.h>

int main(void) {
	int a,b,c,d,n,m,q,r;

	scanf("%d", &n);
	scanf("%d", &m);

	a=100-n;
	b=100-m;
	c=100-a-b;
	d=a*b;
	q=d/100;
	r=d%100;


	printf("%d %d %d %d %d %d\n", a,b,c,d,q,r);
	if (d>=100){
		printf("%d %d", c+q, r);
	}
	else{
		printf("%d %d", c, d);
	}
	return 0;
}