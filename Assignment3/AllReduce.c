#include <mpi.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>
#include <string.h>
#include <sys/time.h>

int elapsedTime(struct timeval t1, struct timeval t2) {
	return (t2.tv_sec-t1.tv_sec)*1000000 + (t2.tv_usec-t1.tv_usec);
}

int* GenerateArray(int size, int rank){
	
	srand(rank);
	int *subArray = (int *)malloc(sizeof(int) * size);

    for (int i = 0; i < size; i++)
    	subArray[i] = (int)(rand() % 1000);

    return subArray;
}


int MPILibraryAllReduce(int rank, int size, int *subArray, int choice){

	int local_output = subArray[0];
	int global_output = 0; 

	for (int i = 1; i < size; i++){
		if(choice == 1)
			local_output += subArray[i];
		if(choice == 2)
			local_output = (local_output > subArray[i]) ? local_output : subArray[i];
	}

	if(choice == 1)
		MPI_Allreduce(&local_output, &global_output, 1, MPI_INT, MPI_SUM, MPI_COMM_WORLD);
	if(choice == 2)
		MPI_Allreduce(&local_output, &global_output, 1, MPI_INT, MPI_MAX, MPI_COMM_WORLD);

	printf("Rank: %d, Global: %d\n", rank, global_output);
	return global_output;
}

int main(int argc, char** argv) {
    int rank, p, i, global_output;
    struct timeval t1, t2;


    MPI_Init(NULL, NULL);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &p);

    assert(argc == 4);

    int n = atoi(argv[1]);
    int func = atoi(argv[2]);																			// 1 for MyAllReduce, 2 for NaiveAllReduce, 3 for MPILibraryAllReduce
    int op = atoi(argv[3]);																				// 1 for add, 2 for max

    assert(n % p == 0);    
    assert(n > p);

    int size = (int) n / p;

    int *subArray = GenerateArray(size, rank);
    
    gettimeofday(&t1, NULL);
    if (func == 3)
    	global_output = MPILibraryAllReduce(rank, size, subArray, op);

    gettimeofday(&t2, NULL);





    free(subArray);

    MPI_Barrier(MPI_COMM_WORLD);
    MPI_Finalize();
}