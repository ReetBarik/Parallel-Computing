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
    } while(strncmp("# Nodes: ", buffer, 9) != 0);

    t = strtok(buffer + 9, " \t");
    count = atoi(t);

    while(buffer[0] == '#')
        s.getline(buffer, 256);

    al = std::vector <std::vector <int> >(count, std::vector<int>(0));

    while(!s.eof()) {
        if (count == 4039)
            t = strtok(buffer, " ");
        else
        	t = strtok(buffer, "\t");
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
        return al.at(node);
    else 
        return std::vector<int>();
}