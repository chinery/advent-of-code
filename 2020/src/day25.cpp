#include "day25.hpp"

Day25::Day25() : Solver("day25") {}

std::string Day25::runPart1(const std::vector<std::string>& input) {
    int cardPK = std::stoi(input[0]);
    int doorPK = std::stoi(input[1]);

    int subjnum = 7;

    int cardLS = 0;
    int doorLS = 0;

    int loopSize = 0;
    long value = 1;
    while(cardLS == 0 && doorLS == 0) {
        value = (value * subjnum) % 20201227;
        loopSize++;

        if(value == cardPK) cardLS = loopSize;
        if(value == doorPK) doorLS = loopSize;
    }

    if(cardLS == 0) {
        loopSize = doorLS;
        subjnum = cardPK;
    } else {
        loopSize = cardLS;
        subjnum = doorPK;
    }

    value = 1;
    while(loopSize > 0) {
        value = (value * subjnum) % 20201227;
        loopSize--;
    }

    return std::to_string(value);
}

std::string Day25::runPart2(const std::vector<std::string>& input) {
    return "Merry Xmas!";
}