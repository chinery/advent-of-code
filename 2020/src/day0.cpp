#include "day0.hpp"

Day0::Day0() : Solver("day0") {}

std::string Day0::runPart1(const std::vector<std::string>& input) {
    long sum = 0;
    for(std::string line : input) {
        sum += (std::stoi(line) / 3) - 2;
    }
    return std::to_string(sum);
}

std::string Day0::runPart2(const std::vector<std::string>& input) {
    return "";
}