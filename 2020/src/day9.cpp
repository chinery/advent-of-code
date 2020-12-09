#include "day9.hpp"

Day9::Day9() : Solver("day9") {}

std::string Day9::runPart1(const std::vector<std::string>& input) {
    // strictly lower triangular matrix of sums
    int numMat[25][25];
    // last 25 values
    int vals[25];

    for(int i = 0; i < input.size(); i++){
        int val = std::stoi(input[i]);

        if(i >= 25) {
            bool found = false;
            for(int j = 0; j < 25; j++){
                for(int k = 0; k < j; k++) {
                    // check all sums in the lower triangle
                    if(val == numMat[j][k]) {
                        found = true;
                        break;
                    }
                }
                if(found) break;
            }
            if(!found) return std::to_string(val);
        }

        vals[i % 25] = val;
        for(int j = 0; j < 25; j++){
            /*
             * This sets sums in this kind of pattern
             *       i%25
             *        |
             *      X.....
             *      .X....
             *i%25- **X...
             *      ..*X..
             *      ..*.X.
             *      ..*..X
             */
            if(j < i % 25) {
                numMat[i % 25][j] = val + vals[j];
            } else if (j > i % 25) {
                numMat[j][i % 25] = val + vals[j];
            }
        }
    }
    return "-1";
}

std::string Day9::runPart2(const std::vector<std::string>& input) {
    int goal = 144381670;

    // keep track of the total sum, smallest and largest, for every range of numbers
    // up to and including i
    std::vector<int> sums;
    std::vector<int> smallest;
    std::vector<int> largest;

    for(int i = 0; i < input.size(); i++){
        int val = std::stoi(input[i]);

        smallest.push_back(val);
        largest.push_back(val);

        sums.push_back(val);
        for(int j = sums.size() - 2; j >= 0; j--) {
            if(val < smallest[j]) {
                smallest[j] = val;
            }
            if(val > largest[j]) {
                largest[j] = val;
            }

            sums[j] += val;
            if(sums[j] == goal){
                return std::to_string(smallest[j]+largest[j]);
            }
        }
    }

    return "";
}