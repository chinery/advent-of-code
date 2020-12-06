#include "day6.hpp"
#include <set>
#include <iostream>

Day6::Day6() : Solver("day6") {}

std::string Day6::runPart1(const std::vector<std::string>& input) {
    int sum = 0;
    std::set<char> answers;

    for(std::string line : input){
        if(line.empty()){
            answers.clear();
        } else {
            for(char c : line) {
                if(answers.count(c) == 0) {
                    sum++;
                    answers.insert(c);
                }
            }
        }
    }
    return std::to_string(sum);
}

std::string Day6::runPart2(const std::vector<std::string>& input) {
    int sum = 0;
    std::set<char> answers;
    bool newGroup = true;

    for(std::string line : input){
        if(line.empty()){
            sum += answers.size();
            answers.clear();
            newGroup = true;
        } else if(newGroup){
            newGroup = false;
            for(char c : line) {
                answers.insert(c);
            }
        } else {
            for (auto it = answers.begin(); it != answers.end(); ) {
                if(line.find(*it) == std::string::npos) {
                    it = answers.erase(it);
                }
                else {
                    ++it;
                }
            }
        }
    }
    sum += answers.size();
    return std::to_string(sum);
}