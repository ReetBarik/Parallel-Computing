#ifndef PAGERANK_H
#define PAGERANK_H

#include "Reader.h"
#include <omp.h>
#include <cstring>


class PageRank {

	private:
		static Reader list;
		static int rankings[1000000];
		static int K;
        static float D;
        static float runtime;
        static int Assign(void);

    public:
    	static void rank(const char *filename, int K, float D);

};

#endif