#include "day1.hpp"

Day1::Day1() : Solver("day1") {}

std::string Day1::runPart1(const std::vector<std::string>& input) {
    for(std::string line1 : input) {
        for(std::string line2 : input) {
            int num1 = std::stoi(line1);
            int num2 = std::stoi(line2);
            if(num1 + num2 == 2020){
                return std::to_string(num1 * num2);
            }
        }
    }
    return "";
}

std::string Day1::runPart2(const std::vector<std::string>& input) {
    for(std::string line1 : input) {
        for(std::string line2 : input) {
            int num1 = std::stoi(line1);
            int num2 = std::stoi(line2);
            if(num1 + num2 >= 2020) { continue; }

            for(std::string line3 : input) {
                int num3 = std::stoi(line3);
                if(num1 + num2 + num3 == 2020){
                    return std::to_string(num1 * num2 * num3);
                }
            }
        }
    }
    return "";
}