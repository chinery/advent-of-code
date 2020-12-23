#include "day23.hpp"
#include <list>
#include <iostream>
#include <unordered_map>

Day23::Day23() : Solver("day23") {}

std::vector<std::string> Day23::getInput() {
    return {"156794823"};
    // return {"389125467"};
};

std::string Day23::runPart1(const std::vector<std::string>& input) {
    std::list<char> cups(input[0].begin(), input[0].end());
    auto cupPtr = cups.begin();
    char currentCup = *cupPtr;
    auto currentCupPtr = cupPtr;

    for(int turn = 0; turn < 100; turn++){

        if(++cupPtr == cups.end()) {
            cupPtr = cups.begin();
        }
        char pickedUp1 = *(cupPtr);
        cupPtr = cups.erase(cupPtr);

        if(cupPtr == cups.end()) {
            cupPtr = cups.begin();
        }
        char pickedUp2 = *(cupPtr);
        cupPtr = cups.erase(cupPtr);

        if(cupPtr == cups.end()) {
            cupPtr = cups.begin();
        }
        char pickedUp3 = *(cupPtr);
        cupPtr = cups.erase(cupPtr);
        
        char destination = currentCup - 1;
        while(destination == pickedUp1 || destination == pickedUp2 || destination == pickedUp3 || destination == '0') {
            if(destination == '0') {
                destination = '9';
            } else {
                destination--;
            }
        }

        while(*cupPtr != destination){
            if(++cupPtr == cups.end()) {
                cupPtr = cups.begin();
            }
        }

        ++cupPtr;

        cups.insert(cupPtr, pickedUp1);
        cups.insert(cupPtr, pickedUp2);
        cups.insert(cupPtr, pickedUp3);

        if(++currentCupPtr == cups.end()) {
            currentCupPtr = cups.begin();
        }
        cupPtr = currentCupPtr;
        currentCup = *cupPtr;
    }

    std::string ans = "";

    cupPtr = cups.begin();
    while(*cupPtr != '1') ++cupPtr;
    ++cupPtr;
    while(*cupPtr != '1') {
        if(cupPtr == cups.end()) {
            cupPtr = cups.begin();
        } else{
            ans += *cupPtr++;
        }
    }

    return ans;
}

std::string Day23::runPart2(const std::vector<std::string>& input) {
    std::vector<int> cups;
    const int MAX = 1e6;
    cups.reserve(MAX);

    for(int i = 0; i < input[0].length() - 1; i++) {
        cups[input[0][i] - '0'] = input[0][i+1] - '0';
    }

    cups[input[0][input[0].length() - 1] - '0'] = 10;

    for(int i = 10; i < MAX; i++) {
        cups[i] = i + 1;
    }

    cups[MAX] = input[0][0] - '0';

    auto cupPtr = 1;
    int currentCup = input[0][0] - '0';

    for(int turn = 0; turn < 1e7; turn++){
        int pickedUp1 = cups[currentCup];
        int pickedUp2 = cups[pickedUp1];
        int pickedUp3 = cups[pickedUp2];
        int forward4 = cups[pickedUp3];

        cups[currentCup] = forward4;
        
        int destination = currentCup - 1;
        while(destination == pickedUp1 || destination == pickedUp2 || destination == pickedUp3 || destination == 0) {
            if(destination == 0) {
                destination = MAX;
            } else {
                destination--;
            }
        }

        cups[pickedUp3] = cups[destination];
        cups[destination] = pickedUp1;

        currentCup = cups[currentCup];
    }

    long result = (long)cups[1] * cups[cups[1]];

    return std::to_string(result);
}