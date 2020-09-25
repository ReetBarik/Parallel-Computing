  
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <mpi.h> 
#include <assert.h>
#include <math.h>
#include <sys/time.h>


struct timeval t1, t2;

int elapsedTime(struct timeval t1, struct timeval t2) {
	return (t2.tv_sec-t1.tv_sec)*1000000 + (t2.tv_usec-t1.tv_usec);
}


void GenerateInitialGoL(int rank, int n, int p, int *subMatrix){

	MPI_Status status;

	if (rank == 0){
		
		for (int i = 1; i < p; i++){                                  // generate random seeds for process 1 to p

			int seed = (rand() % 93563) + 1;

			gettimeofday(&t1, NULL);
            MPI_Send(&seed, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
	    	gettimeofday(&t2, NULL);

	    	// TODO: stuff with t1 and t2 later
		}

		int seed = (rand() % 93563) + 1;                       // populate subMatrix of rank 0

		for (int i = 0; i < n * n / p; i++){

			if ((rand() % seed) % 2) 
				subMatrix[i] = 0;
			else
				subMatrix[i] = 1;
		}
	}

	else {                                                         // populate subMatrix for ranks 1 to p

		int seed;

		gettimeofday(&t1, NULL);
		MPI_Recv(&seed,1, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
        gettimeofday(&t2, NULL);

        // TODO: stuff with t1 and t2 later

        for (int i = 0; i < n * n / p; i++){

			if ((rand() % seed) % 2) 
				subMatrix[i] = 0;
			else
				subMatrix[i] = 1;
		}
	}

}


void DisplayGoL(int rank, int n, int p, int *subMatrix){

	MPI_Status status;

	if (rank == 0){
		
		int *matrix = (int *)malloc(sizeof(int) * n * n);                             // allocate memory for the whole matrix

		for (int i = 0; i < n * ((int) n / p); i++)                                   // copy subMatrix of rank 0 to the global matrix
			matrix[i] = subMatrix[i];

		for (int i = 1; i < p; i++) {

			int *temp = (int *)malloc(sizeof(int) * n * ((int)n / p));

			MPI_Recv(temp, n * ((int) n / p), MPI_INT, i, MPI_ANY_TAG, MPI_COMM_WORLD, &status);

			int start = i * n * ((int) n / p);
			int end = ((i + 1) * n * ((int) n / p)) - 1;                                // not required

			for (int j = 0; j < n * ((int) n / p); j++)
				matrix[start + j] = temp[j];

			free(temp);                                                                 // deallocate temp only to be allocated again for the next process
		}	

		for (int i = 0; i < n * n; i++){                                                    // display the whole matrix
			
			if (i % n == 0)
				printf("\n");
			printf(" %d ", matrix[i]);
		}	
		printf("\n\n");

	}

	else {

		MPI_Send(subMatrix, n * ((int) n / p), MPI_INT, 0, 0, MPI_COMM_WORLD);

	}
}

int main(int argc, char *argv[]){

	int rank, p, n, G;
	struct timeval t1, t2;
	MPI_Status status;


	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);	                                                  // get current rank
	MPI_Comm_size(MPI_COMM_WORLD, &p);	                                                      // get amount of processes

	assert(argc == 3);						                                                  // making sure of the correct number of input parameters
	assert(p >= 1);                                                                           // making sure that there is at least one process

	n = atoi(argv[1]);          		                                                  // size of matrix
    G = atoi(argv[2]);          		                                                  // #generations to simulate

    assert(n % p == 0);                                                                       // making sure that n is divisible by p

    int *subMatrix = (int*)malloc(sizeof(int) * n * ((int) n / p)); 								      // allocating memeory for the local sub matrix
    

    GenerateInitialGoL(rank, n, p, subMatrix);												  // init

    // TODO: Conditional display later
    DisplayGoL(rank, n, p, subMatrix);                                                        // Concatenate all subMatrix at rank 0 and display

    MPI_Finalize();
    return 0;
}