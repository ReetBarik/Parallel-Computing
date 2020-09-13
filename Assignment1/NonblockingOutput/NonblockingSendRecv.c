#include <stdio.h>
#include <mpi.h> 
#include <assert.h>
#include <sys/time.h>

int main(int argc,char *argv[])
{

	int rank, p, size = 1;
	struct timeval t1, t2;

	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&p);

	printf("my rank=%d\n",rank);
	printf("Rank=%d: number of processes =%d\n",rank,p);

	assert(p>=2);

	while (size <= 2097152) {

		if(rank == 1) {
		 
			char x[size];
			int dest = 0;
			gettimeofday(&t1, NULL);
			MPI_Send(&x, size, MPI_CHAR, dest, 0, MPI_COMM_WORLD);
			gettimeofday(&t2, NULL);
			int tSend = (t2.tv_sec - t1.tv_sec) * 1000000 + (t2.tv_usec - t1.tv_usec);
			   
			printf("Sent,%d,%d\n", size, tSend);

		} else if (rank == 0) {
			
			char y[size];
			MPI_Status status;
			gettimeofday(&t1, NULL);
			MPI_Recv(&y, size, MPI_CHAR, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
			gettimeofday(&t2, NULL);
			int tRecv = (t2.tv_sec - t1.tv_sec) * 1000000 + (t2.tv_usec - t1.tv_usec);

			printf("Received,%d,%d\n", size, tRecv);

		}

		size *= 2;
	}

	MPI_Finalize();
}
