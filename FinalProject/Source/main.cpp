#include "PageRank.h"
#include <assert.h>

int main(int argc, char *argv[]) {

	assert(argc == 5);	   											     // making sure of correct number of arguments

	omp_set_num_threads(atoi(argv[2]));
	std::cout << "Input File: " << argv[1] << std::endl;
	std::cout << "Parameters:" << std::endl;
    std::cout << "#Threads: " << atoi(argv[2]) << ", Walk Length: " << atoi(argv[3]) << ", Damping Ratio: " << atof(argv[4]) << std::endl;
	PageRank::rank(argv[1], atoi(argv[3]), atof(argv[4]));

	return 0;
}