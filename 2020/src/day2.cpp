#include "day2.hpp"
#include <sstream>
#include <algorithm>

Day2::Day2() : Solver("day2") {}

int Day2::processAndCount(const std::vector<std::string>& input, int part) {
    int correctCount = 0;
    for(std::string line1 : input) {
        // using getline rather than sscanf to parse string
        // more lines but neatly handles variable length password

        std::stringstream lineStream(line1);
        int low, high;
        char ruleChar;
        std::string password;
        std::string temp;

        std::getline(lineStream, temp, '-');
        low = std::stoi(temp);

        std::getline(lineStream, temp, ' ');
        high = std::stoi(temp);

        std::getline(lineStream, temp, ':');
        ruleChar = temp[0];

        std::getline(lineStream, temp);
        password = temp.substr(1, std::string::npos);

        // std::cout << low << ',' << high << ',' << ruleChar << ',' << password << std::endl;

        if(part == 1) {
            int count = std::count(password.begin(), password.end(), ruleChar);
            if(count >= low && count <= high)
                correctCount++;
        } else {
            if(password[low-1] == ruleChar ^ password[high-1] == ruleChar)
                correctCount++;
        }
    }
    return correctCount;
}

std::string Day2::runPart1(const std::vector<std::string>& input) {
    int correctCount = processAndCount(input, 1);
    return std::to_string(correctCount);
}

std::string Day2::runPart2(const std::vector<std::string>& input) {
    int correctCount = processAndCount(input, 2);
    return std::to_string(correctCount);
}