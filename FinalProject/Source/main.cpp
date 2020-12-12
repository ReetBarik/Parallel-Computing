#include "PageRank.h"
#include <assert.h>

int main(int argc, char *argv[]) {

	assert(argc == 5);	   											     // making sure of correct number of arguments

	omp_set_num_threads(atoi(argv[2]));
	PageRank::rank(argv[1], atoi(argv[3]), atof(argv[4]));

	return 0;
}