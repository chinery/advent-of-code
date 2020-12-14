#include "day13.hpp"
#include "util.hpp"
#include <iostream>

Day13::Day13() : Solver("day13") {}

std::string Day13::runPart1(const std::vector<std::string>& input) {
    int minTime = std::stoi(input[0]);
    auto busses = util::split(input[1], ',');
    int bestTime = 9999999;
    int bestBus = 0;
    for(auto& bus : busses){
        if(bus != "x") {
            int busNum = std::stoi(bus);
            int busTime = ((minTime / busNum) + 1) * busNum;
            if(busTime - minTime < bestTime){
                bestTime = busTime - minTime;
                bestBus = busNum;
            }
        }
    }
    return std::to_string(bestTime * bestBus);
}

// from https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
// doing CRT manually was enough for now
int modInverse(int a, int m) 
{ 
    int m0 = m; 
    int y = 0, x = 1; 
  
    if (m == 1) 
        return 0; 
  
    while (a > 1) { 
        // q is quotient 
        int q = a / m; 
        int t = m; 
  
        // m is remainder now, process same as 
        // Euclid's algo 
        m = a % m, a = t; 
        t = y; 
  
        // Update y and x 
        y = x - q * y; 
        x = t; 
    } 
  
    // Make x positive 
    if (x < 0) 
        x += m0; 
  
    return x; 
} 

std::string Day13::runPart2(const std::vector<std::string>& input) {
    auto busses = util::split(input[1], ',');
    
    std::vector<std::pair<int, int>> busDetails;

    std::vector<long> parts;
    for(int i = 0; i < busses.size(); i++){
        auto& bus = busses[i];
        if(bus != "x") {
            int busNum = std::stoi(bus);
            
            int value = (busNum - i)%busNum;
            while(value < 0) value += busNum;
            
            busDetails.push_back({value, busNum});
            parts.push_back(1);
        }
    }

    // Chinese remainder part one (mod x)
    for(int i = 0; i < parts.size(); i++){
        for(int j = 0; j < parts.size(); j++) {
            if(i != j || busDetails[j].first == 0) {
                parts[i] *= busDetails[j].second;
            }
        }
    }

    // Chinese remainder part two (x mod)
    for(int i = 0; i < parts.size(); i++){
        int current = parts[i] % busDetails[i].second;
        if(current != busDetails[i].first) {
            parts[i] *= modInverse(current, busDetails[i].second);
            parts[i] *= busDetails[i].first;
        }
    }

    long sum = 0;
    long mod = 1;
    for(int i = 0; i < parts.size(); i++){
        sum += parts[i];
        mod *= busDetails[i].second;
    }

    return std::to_string(sum % mod);

    // for(auto& pair : busDetails){
    //     std::cout << pair.first << ',';
    // }

    // std::cout << std::endl;

    // for(auto& pair : busDetails){
    //     std::cout << pair.second << ',';
    // }

    // return "";
}