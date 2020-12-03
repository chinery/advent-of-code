#include "day3.hpp"

Day3::Day3() : Solver("day3") {}

int Day3::countTrees(const std::vector<std::string>& input, int moveDown, int moveRight){
    int row = 0, col = 0;
    int trees = 0;
    size_t width = input[0].size();

    while(row < input.size()){
        row = row + moveDown;
        col = (col + moveRight) % width;

        if(input[row][col] == '#')
            trees++;
    }
    return trees;
}

std::string Day3::runPart1(const std::vector<std::string>& input) {
    return std::to_string(countTrees(input, 1, 3));
}

std::string Day3::runPart2(const std::vector<std::string>& input) {
    /*
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.*/
    long result = (long)countTrees(input, 1, 1) * 
                    countTrees(input, 1, 3) * 
                    countTrees(input, 1, 5) * 
                    countTrees(input, 1, 7) * 
                    countTrees(input, 2, 1);
    return std::to_string(result); 
}