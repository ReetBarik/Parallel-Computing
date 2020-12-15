#ifndef PAGERANK_H
#define PAGERANK_H

#include "Reader.h"
#include <omp.h>
#include <cstring>


class PageRank {

	private:
		static Reader list;																		// Adjacency List
		static int rankings[1000000];															// List of node Ranks
		static int K;																			// Walk Length
        static float D;																			// Damping Ratio

    public:
    	static void rank(const char *filename, int K, float D);
    	static void displayTop5(Reader l, int top5[], int index[], double time);

};

#endif