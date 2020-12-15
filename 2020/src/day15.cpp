#include "day15.hpp"
#include "util.hpp"
#include <unordered_map>
#include <iostream>
#include <algorithm>

Day15::Day15() : Solver("day15") {}

std::vector<std::string> Day15::getInput() {
    return {"17,1,3,16,19,0"};
    // return {"0,3,6"};
};

/*
 * v1 (run) uses an unordered map to store [num] -> turn last spoken
 * memory efficient but takes ~25 s to run due to hash calculations
 * v2 (run2) simply uses a heap allocated array that is large enough to do the same thing
 * for part 2 this means storing an array of 30,000,000 ints ≈ 120MB
 * but total time to run part 1 + part 2 = 0.76 s
 */ 

std::string run(const std::vector<std::string>& input, int stop) {
    std::vector<std::string> numbers = util::split(input[0], ',');
    std::unordered_map<int, int> lastSeen;
    lastSeen.reserve(stop);

    int i = 1;
    int num;
    for(const std::string& numStr : numbers){
        num = std::stoi(numStr);
        lastSeen[num] = i;
        i++;
    } 

    int next = 0;

    while(i <= stop){
        num = next;
        if(lastSeen.find(num) != lastSeen.end()) {
            next = i - lastSeen[num];
        } else {
            next = 0;
        }
        lastSeen[num] = i;
        i++;
    }
    return std::to_string(num);
}

std::string run2(const std::vector<std::string>& input, size_t stop) {
    std::vector<std::string> numbers = util::split(input[0], ',');
    int* lastSeen = new int[stop] {};

    // using a vector, even with preallocated size, takes about 2-3x as long
    // std::vector<int> lastSeen(stop, 0);

    int i = 1;
    int num;
    for(const std::string& numStr : numbers){
        num = std::stoi(numStr);
        lastSeen[num] = i;
        i++;
    } 

    int next = 0;

    while(i <= stop){
        num = next;
        if(lastSeen[num] != 0) {
            next = i - lastSeen[num];
        } else {
            next = 0;
        }
        lastSeen[num] = i;
        i++;
    }

    delete[] lastSeen;
    return std::to_string(num);
}

std::string Day15::runPart1(const std::vector<std::string>& input) {
    return run2(input, 2020);
}

std::string Day15::runPart2(const std::vector<std::string>& input) {
    return run2(input, 30000000);
}