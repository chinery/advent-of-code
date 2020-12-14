#include "day14.hpp"
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <bitset>

Day14::Day14() : Solver("day14") {}

std::string Day14::runPart1(const std::vector<std::string>& input) {
    std::unordered_map<int, long> memory; 
    std::string mask;
    unsigned long maskOnes, maskZeros;
    for(auto& line : input){
        if(line.substr(0, 4) == "mask"){
            mask = line.substr(7);
            std::string maskone = mask;
            std::string maskzero = mask;
            std::replace(maskone.begin(), maskone.end(), 'X', '0');
            std::replace(maskzero.begin(), maskzero.end(), 'X', '1');
            maskOnes = std::stoul(maskone, 0, 2);
            maskZeros = std::stoul(maskzero, 0, 2);
        } else{
            
            unsigned int address = std::stoi(line.substr(4, line.find(']') - 4));
            unsigned long val = std::stoi(line.substr(line.find('=') + 2));

            val |= maskOnes;
            val &= maskZeros;

            memory[address] = val; 
        }
    }

    long sum = 0;
    for(auto& mem : memory) {
        sum += mem.second;
    }
    return std::to_string(sum);
}

// nothing particularly clever about part 2, I just simulate it!
void setAllCombos(std::bitset<36>& address, std::vector<int>& xes, int ix, std::unordered_map<long, long>& memory, long value) {
    if(ix == xes.size()) {
        memory[address.to_ulong()] = value;
        return;
    }

    address[xes[ix]] = 0;
    setAllCombos(address, xes, ix + 1, memory, value);

    address[xes[ix]] = 1;
    setAllCombos(address, xes, ix + 1, memory, value);
}

std::string Day14::runPart2(const std::vector<std::string>& input) {
    std::unordered_map<long, long> memory; 
    std::string mask;
    unsigned long maskOnes;
    std::vector<int> xes;
    for(auto& line : input){
        if(line.substr(0, 4) == "mask"){
            mask = line.substr(7);
            std::string maskone = mask;

            xes.clear();
            for(int i = 0; i < mask.length(); i++) {
                if(mask[i] == 'X') {
                    xes.push_back(35-i);
                }
            }

            std::replace(maskone.begin(), maskone.end(), 'X', '0');
            maskOnes = std::stoul(maskone, 0, 2);
        } else{
            std::bitset<36> address(std::stoi(line.substr(4, line.find(']') - 4)));
            unsigned int val = std::stoi(line.substr(line.find('=') + 2));
            
            address |= maskOnes;

            setAllCombos(address, xes, 0, memory, val);
        }
    }

    long sum = 0;
    for(auto& mem : memory) {
        sum += mem.second;
    }
    return std::to_string(sum);
}