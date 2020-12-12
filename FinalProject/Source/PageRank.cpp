#include "PageRank.h"


Reader PageRank::list = Reader();
int PageRank::K = 1;
int PageRank::rankings[1000000];
float PageRank::D = 0.0;
float PageRank::runtime = 0.0;



void PageRank::rank(const char * filename, int k, float d) {
    std::fstream f;
    int top5[5] = {0, 0, 0, 0, 0}, top_5_idx[5] = {0, 0, 0, 0, 0};

    f.open(filename);

    list = Reader(f);
    K = k;
    D = d;

    int i, j, node_cnt, next_node;
    std::vector<int> curr_node;
    double random;
    struct drand48_data r_buff;

    node_cnt = list.al.size();
    memset(rankings, 0, 1000000);
    srand48_r((int)time(0), &r_buff);
    #pragma omp parallel for schedule(static) private(curr_node, next_node, r_buff, random)
    for(i = 0; i < node_cnt; i++ ) {
    	curr_node = list.adjacent(i);
    	for(int j = 0; j < K; j++) {
    		drand48_r(&r_buff, &random);

    		if(curr_node.size() == 0 || random <= D) {
                drand48_r(&r_buff, &random);
                next_node = (int)(random * node_cnt);
            } else {
                drand48_r(&r_buff, &random);
                next_node = (int)(random * curr_node.size());
                next_node = curr_node[next_node];
            }

            #pragma omp atomic
            rankings[next_node]++;

            curr_node = list.adjacent(next_node);
    	}
    }

    for(i = 0; i < list.al.size(); i++) {
        for(j = 0; j < 5; j++) {
            if(rankings[i] < top5[j])
                break;
            else {
                if(j > 0) {
                    top5[j - 1] = top5[j];
                    top_5_idx[j - 1] = top_5_idx[j];
                }
                top5[j] = rankings[i];
                top_5_idx[j] = i;
            }
        }
    }

    std::cout << "top5:" << std::endl;
    for (i=0; i < 5; i++) {
        std::cout << 5-i << ". value: " << top5[i] << " node: " << top_5_idx[i] << std::endl;
    }

}

