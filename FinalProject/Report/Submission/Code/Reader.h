#ifndef READ_H
#define READ_H

#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>
#include <vector>


class Reader{

	public:
		std::vector< std::vector<int> > al;							// inside public to do away with having to write functions for accessing
		Reader();
		Reader(std::fstream &s);
		std::vector<int> adjacent(const int node) const;			// to get the list of neighbors of a node
};

#endif