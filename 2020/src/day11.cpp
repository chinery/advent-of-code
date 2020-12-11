#include "day11.hpp"
#include <algorithm>
#include <iostream>

Day11::Day11() : Solver("day11") {}

int countAdjacent(const std::vector<std::string>& input, int row, int col) {
    int count = 0;
    if(row > 0 && col > 0 && input[row-1][col-1] == '#') count++;
    if(row > 0 && input[row-1][col] == '#') count++;
    if(row > 0 && col < input[0].size() && input[row-1][col+1] == '#') count++;
    if(col > 0 && input[row][col-1] == '#') count++;
    if(col < input[0].size() && input[row][col+1] == '#') count++;
    if(row < input.size() && col > 0 && input[row+1][col-1] == '#') count++;
    if(row < input.size() && input[row+1][col] == '#') count++;
    if(row < input.size() && col < input[0].size() && input[row+1][col+1] == '#') count++;
    return count;
}

std::vector<std::string> simulateStep(const std::vector<std::string>& input) {
    std::vector<std::string> stepped = input;
    for(int i = 0; i < input.size(); i++){
        for(int j = 0; j < input[0].size(); j++){
            if(input[i][j] == 'L' && countAdjacent(input, i, j) == 0) {
                stepped[i][j] = '#';
            } else if(input[i][j] == '#' && countAdjacent(input, i, j) >= 4) {
                stepped[i][j] = 'L';
            }
        }
    }
    return stepped;
}

std::string Day11::runPart1(const std::vector<std::string>& input) {
    // this feels like an unnecessary number of copies, but I tried using two vectors
    // and allocating values back and forth and it was slightly slower

    std::vector<std::string> prev = input;
    std::vector<std::string> step = simulateStep(prev);

    while(prev != step){
        prev = step;
        step = simulateStep(prev);
    }

    int count = 0;
    for(std::string row : step) {
        count += std::count(row.begin(), row.end(), '#');
    }

    return std::to_string(count);
}

bool searchDirection(const std::vector<std::string>& input, int i_row, int i_col, int d_row, int d_col){
    int row = i_row;
    int col = i_col;
    while((row+d_row) >= 0 && (col+d_col) >= 0 && (row+d_row) < input.size() && (col+d_col) < input[0].size() && input[row+d_row][col+d_col] == '.'){
        row += d_row;
        col += d_col;
    }
    return (row+d_row) >= 0 && (col+d_col) >= 0 && (row+d_row) < input.size() && (col+d_col) < input[0].size() && input[row+d_row][col+d_col] == '#';
}


int countAdjacent2(const std::vector<std::string>& input, int i_row, int i_col, int goal) {
    int count = 0;

    const static int direction[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

    for(int d = 0; d < 8; d++){
        count += searchDirection(input, i_row, i_col, direction[d][0], direction[d][1]);
        if(count >= goal) return count;
    }

    return count;
}

std::vector<std::string> simulateStep2(const std::vector<std::string>& input) {
    std::vector<std::string> stepped = input;
    for(int i = 0; i < input.size(); i++){
        for(int j = 0; j < input[0].size(); j++){
            if(input[i][j] == 'L' && countAdjacent2(input, i, j, 1) == 0) {
                stepped[i][j] = '#';
            } else if(input[i][j] == '#' && countAdjacent2(input, i, j, 5) >= 5) {
                stepped[i][j] = 'L';
            }
        }
    }

    return stepped;
}

std::string Day11::runPart2(const std::vector<std::string>& input) {
    std::vector<std::string> prev = input;
    std::vector<std::string> step = simulateStep2(prev);

    while(prev != step){
        prev = step;
        step = simulateStep2(prev);
    }

    int count = 0;
    for(const std::string& row : step) {
        count += std::count(row.begin(), row.end(), '#');
    }

    return std::to_string(count);
}