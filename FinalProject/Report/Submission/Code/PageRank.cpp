#include "PageRank.h"


Reader PageRank::list = Reader();
int PageRank::K = 1;
int PageRank::rankings[1000000];
float PageRank::D = 0.0;


void PageRank::displayTop5(Reader l, int top5[], int index[], double time) {

	for(int i = 0; i < list.al.size(); i++) {
        for(int j = 0; j < 5; j++) {
            if(rankings[i] < top5[j])
                break;
            else {
                if(j > 0) {
                    top5[j - 1] = top5[j];
                    index[j - 1] = index[j];
                }
                top5[j] = rankings[i];
                index[j] = i;
            }
        }
    }
    std::cout << "Time taken: " << time << " Milliseconds" << std::endl; 
    std::cout << "Rankings:" << std::endl;
    for (int i=0; i < 5; i++) {
        std::cout << "Rank: " << 5-i << ", Page Rank: " << top5[i] << ", Node ID: " << index[i] << std::endl;
    }
}


void PageRank::rank(const char *filename, int k, float d) {
    
    int top5[5] = {0, 0, 0, 0, 0}, index[5] = {0, 0, 0, 0, 0};									// top5 stores the PageRanks, index stores the node
    std::fstream f;

    f.open(filename);

    list = Reader(f);
    K = k;
    D = d;

    int count, next;
    std::vector<int> current;
    double random;
    struct drand48_data randomBuffer;

    count = list.al.size();																		// total number of nodes in the graph
    memset(rankings, 0, 1000000);																// all are ranked 0 at the beginning
    srand48_r((int)time(0), &randomBuffer);

    double t1 = omp_get_wtime();
    #pragma omp parallel for schedule(static) private(current, next, randomBuffer, random)
    for(int i = 0; i < count; i++ ) {															// parallel random walks from each node
    	current = list.adjacent(i);
    	for(int j = 0; j < K; j++) {															// random walk of length K
    		drand48_r(&randomBuffer, &random);

    		if(current.size() == 0 || random <= D) {
                drand48_r(&randomBuffer, &random);
                next = (int)(random * count);													// Damping out to next node
            } else {
                drand48_r(&randomBuffer, &random);
                next = (int)(random * current.size());
                next = current[next];															// Walking to a random neighbor of the current node
            }

            #pragma omp atomic
            rankings[next]++;																	// increase rank of 'next' by 1 (atomic)

            current = list.adjacent(next);														// set 'current' as 'next'
    	}
    }
    double t2 = omp_get_wtime();

    displayTop5(list, top5, index, (t2 - t1) * 1000);											// Display results

}

