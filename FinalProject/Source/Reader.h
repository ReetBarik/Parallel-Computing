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
		std::vector< std::vector<int> > al;
		Reader();
		Reader(std::fstream &s);
		std::vector<int> adjacent(const int node) const;
};

#endif