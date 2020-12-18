#include "day18.hpp"
#include <list>

// fun with recursion and iterators!
// huh the code worked on the first try, how unexpected.
long evaluateMaths2(std::string input, int& i) {
    std::list<long> expression;

    for(; i < input.length(); i++){
        if(input[i] == ' '){
            continue;
        } else if(input[i] == '(') {
            expression.push_back(evaluateMaths2(input, ++i));
        } else if(input[i] == ')') {
            break;
        } else if(input[i] == '+') {
            expression.push_back(-1);
        } else if(input[i] == '*') {
            expression.push_back(-2);
        } else {
            expression.push_back(input[i] - '0');
        }
    }

    auto it = expression.begin();
    while(it != expression.end()) {
        if(*it == -1) {
            auto prev = std::prev(it);
            auto next = std::next(it);

            expression.insert(prev, *prev + *next);
            expression.erase(prev);
            expression.erase(it);
            it = expression.erase(next);
        } else {
            ++it;
        }
    }

    it = expression.begin();
    while(it != expression.end()) {
        if(*it == -2) {
            auto prev = std::prev(it);
            auto next = std::next(it);

            expression.insert(prev, *prev * *next);
            expression.erase(prev);
            expression.erase(it);
            it = expression.erase(next);
        } else {
            ++it;
        }
    }

    return *expression.begin();;
}

enum Op {ADD, TIMES};

long evaluateMaths(std::string input, int& i) {
    long val = 0;
    Op op = ADD;

    for(; i < input.length(); i++){
        long subval = -1;
        if(input[i] == ' '){
            continue;
        } else if(input[i] == '(') {
            subval = evaluateMaths(input, ++i);
        } else if(input[i] == ')') {
            return val;
        } else if(input[i] == '+') {
            op = ADD;
        } else if(input[i] == '*') {
            op = TIMES;
        } else {
            subval = input[i] - '0';
        }

        if(subval > 0 && op == ADD){
            val += subval;
        } else if(subval > 0 && op == TIMES){
            val *= subval;
        }
    }
    return val;
}

long evaluateMaths(std::string input) {
    int i = 0;
    return evaluateMaths(input, i);
}

long evaluateMaths2(std::string input) {
    int i = 0;
    return evaluateMaths2(input, i);
}

Day18::Day18() : Solver("day18") {}

std::string Day18::runPart1(const std::vector<std::string>& input) {
    long total = 0;
    for(const auto& line : input){
        total += evaluateMaths(line);
    }
    return std::to_string(total);
}

std::string Day18::runPart2(const std::vector<std::string>& input) {
    long total = 0;
    for(const auto& line : input){
        total += evaluateMaths2(line);
    }
    return std::to_string(total);
}