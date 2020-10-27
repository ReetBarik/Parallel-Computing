#include <mpi.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>
#include <string.h>
#include <sys/time.h>

int elapsedTime(struct timeval t1, struct timeval t2) {													// Helper function to calculate time taken in Microseconds
	return (t2.tv_sec-t1.tv_sec)*1000000 + (t2.tv_usec-t1.tv_usec);
}

int op(int a, int b, int choice){																		// Helper function to perform the operation of choice in MyAllReduce
	if(choice == 1)
		return (a + b);
	if(choice == 2)
		return (a > b) ? a : b;
}

int* GenerateArray(int size, int rank){																	// Generate an array of random numbers < 1000 of size 'size'
	
	srand(rank);
	int *subArray = (int *)malloc(sizeof(int) * size);

    for (int i = 0; i < size; i++)
    	subArray[i] =(int)(rand() % 1000);

    return subArray;
}

int computeLocal(int size, int *subArray, int choice){													// Helper function to calculate partial output of the SubArray
	
	int local_output = subArray[0];

	for (int i = 1; i < size; i++){
		if(choice == 1)
			local_output += subArray[i];
		if(choice == 2)
			local_output = (local_output > subArray[i]) ? local_output : subArray[i];
	}

	return local_output;
}


int MyAllReduce(int rank, int size, int *subArray, int choice, int p){

	int global_output, partner, k = 1;
	MPI_Status status;

	int local_output = computeLocal(size, subArray, choice);

	if (p == 1) {																						// Local sum == Global Sum
		// printf("Rank: %d, Global: %d\n", rank, local_output);
		return local_output;
	}
	else 
	{

		for (int t = 0; t < ceil(log2(p)); t++) {														// iterate through log2(p) steps
			partner = rank ^ k;																			// XOR
			k << 1;																						// bitshift 
			MPI_Sendrecv(&local_output, 1, MPI_INT, partner, 0, &global_output, 1, MPI_INT, partner, 0, MPI_COMM_WORLD, &status);    // exchange with partner process
			local_output = op(global_output, local_output, choice);										// compute local sum for that time step
		}

		global_output = local_output;																	// Global Sum
		// printf("Rank: %d, Global: %d\n", rank, global_output);										// For testing AllReduce indeed does the 'All' part and doesn't just do reduce
		return global_output;
	}
	
}


int NaiveAllReduce(int rank, int size, int *subArray, int choice, int p){
	
	int global_output, recv, send;
    MPI_Status status;

	int local_output = computeLocal(size, subArray, choice);

	if (p == 1) {																						// Local sum == Global Sum
		// printf("Rank: %d, Global: %d\n", rank, local_output);
		return local_output;
	}
	else 
	{
        if (rank == 0)
        	MPI_Send(&local_output, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);									// Only send if you are rank 0
        else {
        	MPI_Recv(&recv, 1, MPI_INT, rank - 1, 0, MPI_COMM_WORLD, &status);							// recv from rank - 1
        	local_output += recv;																		// Compute local partial sum
        	if (rank < p - 1)
        		MPI_Send(&local_output, 1, MPI_INT, rank + 1, 0, MPI_COMM_WORLD);						// send to rank + 1. Do nothing if you are rank == p - 1
        }

        MPI_Barrier(MPI_COMM_WORLD);																	// All processes wait till the global sum is computed in rank p - 1

        if (rank == p - 1)
        	MPI_Send(&local_output, 1, MPI_INT, rank - 1, 0, MPI_COMM_WORLD);							// Send to rank - 1 if you are rank p - 1
        else {
        	if (rank == 0)
        		MPI_Recv(&local_output, 1, MPI_INT, rank + 1, 0, MPI_COMM_WORLD, &status);				// Only recv if you are rank 0
        	else {
	        	MPI_Recv(&local_output, 1, MPI_INT, rank + 1, 0, MPI_COMM_WORLD, &status);				// recv and forward if you are anything in between 0 and p - 1
	        	MPI_Send(&local_output, 1, MPI_INT, rank - 1, 0, MPI_COMM_WORLD);
	        }
        }

        global_output = local_output;
        // printf("Rank: %d, Global: %d\n", rank, global_output);										// For testing AllReduce indeed does the 'All' part and doesn't just do reduce
		return global_output;
	}

}



int MPILibraryAllReduce(int rank, int size, int *subArray, int choice, int p){
	
	int global_output = 0; 

	int local_output = computeLocal(size, subArray, choice);

	if(choice == 1)
		MPI_Allreduce(&local_output, &global_output, 1, MPI_INT, MPI_SUM, MPI_COMM_WORLD);
	if(choice == 2)
		MPI_Allreduce(&local_output, &global_output, 1, MPI_INT, MPI_MAX, MPI_COMM_WORLD);
	
	// printf("Rank: %d, Global: %d\n", rank, global_output);											// For testing AllReduce indeed does the 'All' part and doesn't just do reduce	
	return global_output;
}



int main(int argc, char** argv) {
    int rank, p, i, global_output, time;
    struct timeval t1, t2;

    MPI_Init(NULL, NULL);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &p);

    assert(argc == 4);

    int n = atoi(argv[1]);																				// Size of Array
    int func = atoi(argv[2]);																			// 1 for MyAllReduce, 2 for NaiveAllReduce, 3 for MPILibraryAllReduce
    int op = atoi(argv[3]);																				// 1 for add, 2 for max

    assert(n % p == 0);    
    assert(n > p);

    int size = (int) n / p;																				// Size of SubArray

    int *subArray = GenerateArray(size, rank);

    gettimeofday(&t1, NULL);

    if (func == 1)
    	global_output = MyAllReduce(rank, size, subArray, op, p);
    if (func == 2)
    	global_output = NaiveAllReduce(rank, size, subArray, op, p);
    if (func == 3)
    	global_output = MPILibraryAllReduce(rank, size, subArray, op, p);

    gettimeofday(&t2, NULL);

    time = elapsedTime(t1, t2);

    int *times;
    if (rank == 0)
    	times = (int *)malloc(p * sizeof(int)); 

    MPI_Gather(&time, 1, MPI_INT, times, 1, MPI_INT, 0, MPI_COMM_WORLD);								// Collecting the largest of the times from across the processes

    if (rank == 0){																						// Output in Rank 0 only instead of all processes
    	int max = time;
    	for (i = 0; i < p - 1; i++){
    		if (times[i] > max)
    			max = times[i];
    	}

	    printf("Timing Statistics:\n");
	    printf("Size of Array: %d\n", n);
	    printf("Number of processes: %d\n", p);
	    if (op == 1)
	    	printf("Binary Associative Operator: ADD\n");
	    if (op == 2)
	    	printf("Binary Associative Operator: MAX\n");
	    if (func == 1)
	    	printf("Function: MyAllReduce\n");
	    if (func == 2)
	    	printf("Function: NaiveAllReduce\n");
	    if (func == 3)
	    	printf("Function: MPILibraryAllReduce\n");
	    printf("Total runtime (in microseconds): %d\n", max);
	    printf("Global Output: %d\n", global_output);
	    free(times);
	}

    free(subArray);

    MPI_Finalize();
    return 0;
}