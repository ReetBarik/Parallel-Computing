#include "Reader.h"

Reader::Reader() {
	al = std::vector< std::vector <int> >(0);
}

Reader::Reader(std::fstream &s) {

    int count, current, adj;
    std::string line;
    char *t;
    char buffer[256];

    do {
        s.getline(buffer, 256);
    } while(strncmp("# Nodes: ", buffer, 9) != 0);								// read on till # Nodes is mentioned in the input file header

    t = strtok(buffer + 9, " \t");
    count = atoi(t);															// Graph has 'count' number of nodes

    while(buffer[0] == '#')														// Skip the rest of the headers
        s.getline(buffer, 256);

    al = std::vector <std::vector <int> >(count, std::vector<int>(0));			// empty adjacency list as a vector of vectors

    while(!s.eof()) {															// populate adjacency list
        
        t = strtok(buffer, "\t");												// had to change the delimiter from " " to "\t" in the facebook input
        current = atoi(t);
        if(current > al.size())
        al.resize(current);

        t = strtok(NULL, "\n");
        adj = atoi(t);
        if(adj > al.size())
        al.resize(adj);
        
        al[current].push_back(atoi(t));
        s.getline(buffer, 256);
    }
}


std::vector<int> Reader::adjacent(const int node) const {						

	if(node < al.size())
        return al.at(node);														// return the neighbors of 'node'
    else 
        return std::vector<int>();												// return empty vector if there are no neighbors
}