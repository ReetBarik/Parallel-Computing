#include "omp.h"
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <sys/time.h>
#include <assert.h>

#define PI 3.14159265358979323846										// ground truth value of pi

double estimate(long int darts, int threads) {
	
	long long hits = 0, count = 0; 

	#pragma omp parallel num_threads(threads)  private(hits) reduction(+:count)
	{
		hits = 0; 
		#pragma omp for
		for (long int i = 0; i < darts; i++) {

			int rank = omp_get_thread_num();
			int seed = rank+1;
			seed = seed*i;
			
			double x = ((double)rand_r(&seed) / RAND_MAX) * 2 - 1; 		// random double between -1 and 1
			seed = seed * time(0);
			double y = ((double)rand_r(&seed) / RAND_MAX) * 2 - 1; 		// random double between -1 and 1
			
			if (((x * x) + (y * y)) <= 1)								// x^2 + y^2 <= 1 is internal to the circle
				hits++;
		}
		count += hits;	
	}

	double pi = 4 * ((double)count/(double)darts);
	return pi;
}


int main(int argc, char *argv[]) {

	assert(argc == 3);
	long int n = atol(argv[1]);
	int p = atoi(argv[2]);

	omp_set_num_threads(p);
	double t1 = omp_get_wtime();
	double pi = estimate(n, p);
	double t2 = omp_get_wtime();

	double precision = (fabs(pi - PI) / PI) * 100;
	double runtime = (t2 - t1) * 1000;

	printf("\n");
	printf("n: %ld\n", n);
	printf("p: %d\n", p);
	printf("Pi: %.20lf\n", pi);
	printf("Precision (%% error): %lf\n", precision);
	printf("Time (Milliseconds): %lf\n", runtime);

	// printf("%ld,%d,%lf,%lf\n",n,p,precision,runtime);					// to collect results in a csv

	return 0;
}