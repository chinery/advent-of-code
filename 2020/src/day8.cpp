#include "day8.hpp"
#include <vector>
#include <utility>
#include <set>
#include <iostream>

Day8::Day8() : Solver("day8") {}

std::vector<std::pair<std::string, int>> getProgram(const std::vector<std::string>& input) {
    std::vector<std::pair<std::string, int>> program;
    for(std::string line : input){
        std::string instruction = line.substr(0, 3);
        int value = std::stoi(line.substr(5));
        if(line[4] == '-') value *= -1;

        program.push_back({instruction, value});
    }
    return program;
}

std::string Day8::runPart1(const std::vector<std::string>& input) {
    std::vector<std::pair<std::string, int>> program = getProgram(input);

    std::set<int> visited;
    int pc = 0;
    int acc = 0;
    while(visited.find(pc) == visited.end()){
        visited.insert(pc);
        if(program[pc].first == "acc") {
            acc += program[pc].second;
        } else if(program[pc].first == "jmp") {
            pc += program[pc].second - 1;
        }
        pc += 1;
    }
    return std::to_string(acc);
}

// run the code as if the number^th nop/jmp were changed to a jmp/nop
int runWithModification(const std::vector<std::pair<std::string, int>>& program, int number) {
    std::set<int> visited;
    int pc = 0;
    int acc = 0;
    int count = 0;
    int changedPc = -1;
    while(pc != program.size()){
        // if looped
        if(visited.find(pc) != visited.end()){
            if(changedPc == -1){
                return -2;
            }
            return -1;
        }
        
        if(changedPc == -1 && (program[pc].first == "jmp" || program[pc].first == "nop")) {
            count += 1;
            if(count == number) {
                changedPc = pc;
            }
        }

        visited.insert(pc);
        if(program[pc].first == "acc") {
            acc += program[pc].second;
        } else if(program[pc].first == "jmp" && pc != changedPc) {
            pc += program[pc].second - 1;
        }
        pc += 1;
    }
    return acc;
}

std::string Day8::runPart2(const std::vector<std::string>& input) {
    std::vector<std::pair<std::string, int>> program = getProgram(input);

    int i = 1;
    int acc = runWithModification(program, i);
    while(acc == -1){
        i++;
        acc = runWithModification(program, i);
    }
    return std::to_string(acc);
}