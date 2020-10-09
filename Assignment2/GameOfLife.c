  
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <mpi.h> 
#include <assert.h>
#include <math.h>
#include <sys/time.h>


struct timeval t1, t2;
int communicationTime = 0;
int generationTime = 0, avgGenerationTime;

int elapsedTime(struct timeval t1, struct timeval t2) {
	return (t2.tv_sec-t1.tv_sec)*1000000 + (t2.tv_usec-t1.tv_usec);
}


void GenerateInitialGoL( int rank,  int n,  int p,  int *subMatrix){

	MPI_Status status;

	if (rank == 0){
		
		for ( int i = 1; i < p; i++){                                  											// generate random seeds for process 1 to p

			int seed = (rand() % 93563) + 1;

			gettimeofday(&t1, NULL);
            MPI_Send(&seed, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
	    	gettimeofday(&t2, NULL);

	    	communicationTime += elapsedTime(t1, t2);
		}

		int seed = (rand() % 93563) + 1;                       													// populate subMatrix of rank 0

		for ( int i = 0; i < n * n / p; i++){

			if ((rand() % seed) % 2) 
				subMatrix[i] = 0;
			else
				subMatrix[i] = 1;
		}
	}

	else {                                                         												// populate subMatrix for ranks 1 to p

		int seed;

		gettimeofday(&t1, NULL);
		MPI_Recv(&seed,1, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
        gettimeofday(&t2, NULL);

        communicationTime += elapsedTime(t1, t2);

        for ( int i = 0; i < n * n / p; i++){

			if ((rand() % seed) % 2) 
				subMatrix[i] = 0;
			else
				subMatrix[i] = 1;
		}
	}

}


void DisplayGoL( int rank,  int n,  int p,  int *subMatrix){

	MPI_Status status;

	if (rank == 0){
		
		int *matrix = ( int *)malloc(sizeof( int) * n * n);                             						// allocate memory for the whole matrix

		for ( int i = 0; i < n * (( int) n / p); i++)                                   						// copy subMatrix of rank 0 to the global matrix
			matrix[i] = subMatrix[i];

		for ( int i = 1; i < p; i++) {

			int *temp = ( int *)malloc(sizeof( int) * n * (( int)n / p));

			MPI_Recv(temp, n * (( int) n / p), MPI_INT, i, MPI_ANY_TAG, MPI_COMM_WORLD, &status);

			int start = i * n * (( int) n / p);
			int end = ((i + 1) * n * (( int) n / p)) - 1;                                						// not required

			for ( int j = 0; j < n * (( int) n / p); j++)
				matrix[start + j] = temp[j];

			free(temp);                                                                 						// deallocate temp only to be allocated again for the next process
		}	

		for ( int i = 0; i < n * n; i++){                                                    					// display the whole matrix
			
			if (i % n == 0)
				printf("\n");
			printf(" %d ", matrix[i]);
		}	
		printf("\n\n");

	}

	else {

		MPI_Send(subMatrix, n * (( int) n / p), MPI_INT, 0, 0, MPI_COMM_WORLD);

	}
}




int DetermineState( int pos,  int *next,  int *previous,  int *subMatrix,  int n,  int p){

	int N, S, E, W, NE, NW, SE, SW, sum, state;
	if(pos < n){																								// at the top. Needs to use previous
		if (pos == 0){
			N = previous[pos];
			NW = previous[n - 1];
			NE = previous[pos + 1];
			S = subMatrix[pos + n];
			SW = subMatrix[pos + n + n - 1];
			SE = subMatrix[pos + n + 1];
			E = subMatrix[pos + 1];
			W = subMatrix[n - 1];
		}
		else if (pos == n - 1){
			N = previous[pos];
			NW = previous[pos - 1];
			NE = previous[0];
			S = subMatrix[pos + n];
			SW = subMatrix[pos + n - 1];
			SE = subMatrix[pos + 1];
			E = subMatrix[0];
			W = subMatrix[pos - 1];
		}
		else {
			N = previous[pos];
			NW = previous[pos - 1];
			NE = previous[pos + 1];
			S = subMatrix[pos + n];
			SW = subMatrix[pos + n - 1];
			SE = subMatrix[pos + n + 1];
			E = subMatrix[pos + 1];
			W = subMatrix[pos - 1];
		}
	}
	else if (pos > (n * n / p) - 1 - n){																		// at the bottom. Needs to use next
		if (pos % n == 0){
			N = subMatrix[pos - n];
			NW = subMatrix[pos - 1];
			NE = subMatrix[pos - n + 1];
			S = next[0];
			SW = next[n - 1];
			SE = next[1];
			E = subMatrix[pos + 1];
			W = subMatrix[pos + n - 1];
		}
		else if (pos % n == n - 1) {
			N = subMatrix[pos - n];
			NW = subMatrix[pos - n - 1];
			NE = subMatrix[pos - n - n + 1];
			S = next[n - 1];
			SW = next[n - 1 - 1];
			SE = next[0];
			E = subMatrix[pos - n + 1];
			W = subMatrix[pos - 1];
		}
		else {
			N = subMatrix[pos - n];
			NW = subMatrix[pos - n - 1];
			NE = subMatrix[pos - n + 1];
			S = next[pos % n];
			SW = next[pos % n - 1];
			SE = next[pos % n + 1];
			E = subMatrix[pos + 1];
			W = subMatrix[pos - 1];
		}
	}
	else {																										// in the middle

		if (pos % n == 0){ 																						// on the left edge
			N = subMatrix[pos - n];
			NW = subMatrix[pos - 1];
			NE = subMatrix[pos - n + 1];
			S = subMatrix[pos + n];
			SW = subMatrix[pos + n + n - 1];
			SE = subMatrix[pos + n + 1];
			E = subMatrix[pos + 1];
			W = subMatrix[pos + n - 1];
		}
		else if (pos % n == n - 1){																				// on the right edge
			N = subMatrix[pos - n];
			NW = subMatrix[pos - n - 1];
			NE = subMatrix[pos - n - n + 1];
			S = subMatrix[pos + n];
			SW = subMatrix[pos + n - 1];
			SE = subMatrix[pos + 1];
			E = subMatrix[pos - n + 1];
			W = subMatrix[pos - 1];
		}
		else {																									// in the middle
			N = subMatrix[pos - n];
			NW = subMatrix[pos - n - 1];
			NE = subMatrix[pos - n + 1];
			S = subMatrix[pos + n];
			SW = subMatrix[pos + n - 1];
			SE = subMatrix[pos + n + 1];
			E = subMatrix[pos + 1];
			W = subMatrix[pos - 1];
		}
	}

	sum = N + NW + NE + S + SW + SE + E + W;

	if (sum > -1 && sum < 3)
		state = 0;
	if (sum > 2  && sum < 6)
		state = 1;
	if (sum > 5 && sum < 9)
		state = 0;

	return state;
}


void Simulate( int rank,  int n,  int p,  int *subMatrix){

	MPI_Status status;

	int *previous = ( int *)malloc(n * sizeof( int));                                       					// place to store the last row from previous rank
	int *next = ( int *)malloc(n * sizeof( int));                                       						// place to store the first row from next rank
	int *top = ( int *)malloc(n * sizeof( int));                                       							// buffer to store current subMatrix's top row
	int *bottom = ( int *)malloc(n * sizeof( int));                                       						// buffer to store current subMatrix's bottom row

	for ( int i = 0; i < n; i++){
		top[i] = subMatrix[i];																					// copy the top row to buffer
		bottom[i] = subMatrix[((n * n) / p) - n  + i];															// copy the bottom row to buffer
	}

	gettimeofday(&t1, NULL);
    MPI_Send(top, n, MPI_INT, (rank - 1 + p) % p, 0, MPI_COMM_WORLD);	                       					// send top row to previous rank
    MPI_Send(bottom, n, MPI_INT, (rank + 1) % p, 0, MPI_COMM_WORLD);	                       					// send bottom row to next rank

    MPI_Recv(next, n, MPI_INT,(rank + 1) % p, MPI_ANY_TAG, MPI_COMM_WORLD, &status);             				// recv next rank's first row
    MPI_Recv(previous, n, MPI_INT,(rank - 1 + p) % p, MPI_ANY_TAG, MPI_COMM_WORLD, &status);					// recv previous rank's last row
    gettimeofday(&t2, NULL);

    communicationTime += elapsedTime(t1, t2);

    for ( int i = 0; i < n * n / p; i++){
    	subMatrix[i] = DetermineState(i, next, previous, subMatrix, n, p);
    }

    free(previous);
    free(next);
    free(top);
    free(bottom);

}

int main(int argc, char *argv[]){

	int rank, p, n, G;
	MPI_Status status;
	struct timeval g1, g2;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);	                                                  					// get current rank
	MPI_Comm_size(MPI_COMM_WORLD, &p);	                                                      					// get amount of processes

	assert(argc == 3);						                                                  					// making sure of the correct number of input parameters
	assert(p >= 1);                                                                           					// making sure that there is at least one process

	n = atoi(argv[1]);          		                                                  						// size of matrix
    G = atoi(argv[2]);          		                                                  						// #generations to simulate

    assert(n % p == 0);                                                                       					// making sure that n is divisible by p
    assert(n > p);																								// making sure n/p > 1


    int *subMatrix = ( int*)malloc(sizeof( int) * n * (( int) n / p)); 								      		// allocating memeory for the local sub matrix
    
    gettimeofday(&g1, NULL);
    GenerateInitialGoL(rank, n, p, subMatrix);												  					// init
    gettimeofday(&g2, NULL);
    generationTime += elapsedTime(g1, g2);

    for ( int i = 0; i < G; i++){

    	gettimeofday(&g1, NULL);

    	gettimeofday(&t1, NULL);    	
    	MPI_Barrier(MPI_COMM_WORLD);	// block
		gettimeofday(&t2, NULL);
		Simulate(rank, n, p, subMatrix);
		gettimeofday(&g2, NULL);

		communicationTime += elapsedTime(t1, t2);
		generationTime += elapsedTime(g1, g2);

		if (i == 0 || i == 50 || i == 99)                                                                  
    		DisplayGoL(rank, n, p, subMatrix);                                                        			// Concatenate all subMatrix at rank 0 and display

    }

    avgGenerationTime = generationTime / G;

    int *commtimes;
    if (rank == 0)
    	commtimes = ( int *)malloc(p* sizeof( int));

    MPI_Gather(&communicationTime, 1, MPI_INT, commtimes, 1, MPI_INT, 0, MPI_COMM_WORLD);

    int *gentimes;
    if (rank == 0)
    	gentimes = ( int *)malloc(p* sizeof( int));

    MPI_Gather(&generationTime, 1, MPI_INT, gentimes, 1, MPI_INT, 0, MPI_COMM_WORLD);

    if(rank == 0){
    	int maxComm = communicationTime;
    	for ( int i = 0; i < p - 1; i++) {
    		if (commtimes[i] > maxComm) 
    			maxComm = commtimes[i];
    	}  

    
    	int maxGen = generationTime;
    	for ( int i = 0; i < p - 1; i++) {
    		if (gentimes[i] > maxGen) 
    			maxGen = gentimes[i];
    	}

    	printf("Timing Statistics:\n");
    	printf("Size of Matrix: %d X %d\n", n, n);
    	printf("Number of processes: %d\n", p);
    	printf("Number of generations: %d\n", G);
    	printf("Total runtime (in microseconds): %d\n", maxGen);
    	printf("Total runtime per generation (in microseconds): %d\n", maxGen / G);
    	printf("Total communication time (in microseconds): %d\n", maxComm);
    	printf("Total computation time (in microseconds): %d\n", maxGen - maxComm);
    }


    MPI_Finalize();
    return 0;
}