#include "day10.hpp"
#include <set>
#include <iostream>

Day10::Day10() : Solver("day10") {}

std::string Day10::runPart1(const std::vector<std::string>& input) {
    std::set<int> jolts;
    for(const std::string& line : input){
        jolts.insert(std::stoi(line));
    }

    int onediff = 0, threediff = 0;
    int prev = 0;
    for(const int& jolt : jolts){
        if(jolt - prev == 1){
            onediff++;
        } else if(jolt - prev == 3) {
            threediff++;
        }
        prev = jolt;
    }
    threediff++;
    return std::to_string(onediff * threediff);
}

std::string Day10::runPart2(const std::vector<std::string>& input) {
    std::set<int> jolts;
    jolts.insert(0);
    for(std::string line : input){
        jolts.insert(std::stoi(line));
    }
    jolts.insert(*jolts.rbegin() + 3);

    long* dp = new long[jolts.size()];
    dp[0] = 1;

    // iterate through the jolts in order
    int i = 1;
    for(auto it = std::next(jolts.begin()); it != jolts.end(); ++it, i++){
        int j = 1;

        // for each one, go backwards up to 3 steps and count those in range
        for(auto bit = it; bit-- != jolts.begin() && j <= 3; j++) {
            if(*bit + 3 >= *it) {
                dp[i] += dp[i-j];
            } else{
                break; 
            }
        }
    }

    long count = dp[jolts.size() - 1];
    delete[] dp;

    return std::to_string(count);
}