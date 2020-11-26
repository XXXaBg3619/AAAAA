#include <stdio.h>
#include <stdlib.h>
#define N_SAMPLES 500000

int main()
{
	float x, y;
	int count = 0;
	srand(30);
	int num = rand();
	
	for (int i=0; i<N_SAMPLES; i++) {
		x = (float)rand()/RAND_MAX;
		y = (float)rand()/RAND_MAX;
		
		if (x*x + y*y <= 1){
			count ++;
		}
	}
	float pi = (float)count / N_SAMPLES * 4;
	printf("%f", pi);
	return 0;
}

