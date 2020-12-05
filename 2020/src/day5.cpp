#include "day5.hpp"
#include <algorithm>
#include <iostream>
#include <set>

Day5::Day5() : Solver("day5") {}

/*
 * I didn't love today's puzzle! Why get me to separate rows and columns when we only need
 * to use the id later? This code could be easily much simpler:
 *  - don't split the strings, change F,L->0 and B,R->1, convert straight to ID
 *  - return a set of ids (or even do the work while parsing)
 * 
 * I'm leaving it like this just in case we need rows and columns in a later puzzle
 */
std::vector<std::pair<int, int>> Day5::parseSeats(const std::vector<std::string>& input) {
    std::vector<std::pair<int, int>> results;
    for(std::string line : input){
        std::string row_s = line.substr(0, 7);
        std::string col_s = line.substr(7);
        std::replace(row_s.begin(), row_s.end(), 'F', '0');
        std::replace(row_s.begin(), row_s.end(), 'B', '1');
        std::replace(col_s.begin(), col_s.end(), 'L', '0');
        std::replace(col_s.begin(), col_s.end(), 'R', '1');

        unsigned long row = std::stoul(row_s, 0, 2);
        unsigned long col = std::stoul(col_s, 0, 2);

        results.push_back({row, col});
    }
    return results;
}

std::string Day5::runPart1(const std::vector<std::string>& input) {
    std::vector<std::pair<int, int>> seats = parseSeats(input);
    int highest = 0;
    for(std::pair<int, int> pair : seats) {
        int id = (pair.first * 8) + pair.second;
        if(id > highest)
            highest = id;
    }
    return std::to_string(highest);
}

std::string Day5::runPart2(const std::vector<std::string>& input) {
    std::vector<std::pair<int, int>> seats = parseSeats(input);
    std::set<int> ids;
    
    for(std::pair<int, int> pair : seats) {
        int id = (pair.first * 8) + pair.second;
        ids.insert(id);
    }

    int temp = 0;
    for(auto it = ids.begin(); it != ids.end(); it++) {
        auto next = std::next(it);
        if(*it + 1 != *next) {
            temp = *it + 1;
        } else if(*it - 1 == temp){
            return std::to_string(temp);
        }   
    }
    return "";
}