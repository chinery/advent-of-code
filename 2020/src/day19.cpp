#include "day19.hpp"
#include "util.hpp"
#include <unordered_map>
#include <iostream>
#include <list>

class Expansion {
private:
    std::vector<int> m_Elements;
public:
    Expansion(std::vector<int> elements) : m_Elements(elements) {}

    bool isChar() {
        return m_Elements[0] > 1000;
    }

    char charValue() {
        return m_Elements[0] - 1000;
    }

    std::vector<int>& elements() {
        return m_Elements;
    }
};

bool parseCFG(const std::string& input, const std::vector<int>& activeRules, const std::unordered_map<int, std::vector<Expansion>>& rules) {
    if(input.size() == 0 || activeRules.size() == 0) return input.size() == 0 && activeRules.size() == 0;

    auto rule = rules.at(activeRules[0]);
    if(rule.size() == 1 && rule[0].isChar()) {
        if(rule[0].charValue() != input[0]){
            return false;
        } else {
            return parseCFG(input.substr(1), std::vector<int>(activeRules.begin() + 1, activeRules.end()), rules);
        }
    } else {
        for(auto expansion : rule) {
            std::vector<int> newActive = expansion.elements();
            newActive.insert(newActive.end(), activeRules.begin() + 1, activeRules.end());
            if(parseCFG(input, newActive, rules)) {
                return true;
            }
        }
        return false;
    }
}

Day19::Day19() : Solver("day19") {}

std::string Day19::runPart1(const std::vector<std::string>& input) {
    std::unordered_map<int, std::vector<Expansion>> rules;
    int count = 0;

    for(const auto& line : input){
        int colon = line.find(':');
        if(colon != std::string::npos) {
            int lhs = std::stoi(line.substr(0, colon));
            if(line[colon + 2] == '"') {
                rules[lhs].push_back(Expansion({line[colon + 3] + 1000}));
            } else {
                std::vector<int> rhsVals = util::split<int>(line.substr(colon + 2), ' ', [](std::string x)->int {
                    if(x == "|") return -1;
                    else return std::stoi(x);
                    });
                if(rhsVals.size() == 1) {
                    rules[lhs].push_back(Expansion({rhsVals[0]}));
                } else if(rhsVals.size() == 3) {
                    rules[lhs].push_back(Expansion({rhsVals[0]}));
                    rules[lhs].push_back(Expansion({rhsVals[2]}));
                } else {
                    rules[lhs].push_back(Expansion({rhsVals[0], rhsVals[1]}));
                    if(rhsVals.size() > 2) {
                        rules[lhs].push_back(Expansion({rhsVals[3], rhsVals[4]}));
                    }
                }
            }
        } else {
            count += parseCFG(line, {0}, rules);
        }
    }

    return std::to_string(count);
}

std::string Day19::runPart2(const std::vector<std::string>& r_input) {
    auto input = r_input;
    input.insert(input.begin(), "8: 42 | 42 8");
    input.insert(input.begin(), "11: 42 31 | 42 11 31");

    std::unordered_map<int, std::vector<Expansion>> rules;
    int count = 0;

    for(const auto& line : input){
        if(line == "8: 42" || line == "11: 42 31") continue;
        
        int colon = line.find(':');
        if(colon != std::string::npos) {
            int lhs = std::stoi(line.substr(0, colon));

            if(line[colon + 2] == '"') {
                rules[lhs].push_back(Expansion({line[colon + 3] + 1000}));
            } else {
                std::vector<int> rhsVals = util::split<int>(line.substr(colon + 2), ' ', [](std::string x)->int {
                    if(x == "|") return -1;
                    else return std::stoi(x);
                    });
                if(rhsVals.size() == 1) {
                    rules[lhs].push_back(Expansion({rhsVals[0]}));
                } else if(rhsVals.size() == 3) {
                    rules[lhs].push_back(Expansion({rhsVals[0]}));
                    rules[lhs].push_back(Expansion({rhsVals[2]}));
                } else if(rhsVals.size() == 4) { //this is where I start to wish I'd just split on '|'
                    rules[lhs].push_back(Expansion({rhsVals[0]}));
                    rules[lhs].push_back(Expansion({rhsVals[2], rhsVals[3]}));
                } else if(rhsVals.size() == 6) {
                    rules[lhs].push_back(Expansion({rhsVals[0], rhsVals[1]}));
                    rules[lhs].push_back(Expansion({rhsVals[3], rhsVals[4], rhsVals[5]}));
                } else {
                    rules[lhs].push_back(Expansion({rhsVals[0], rhsVals[1]}));
                    if(rhsVals.size() > 2) {
                        rules[lhs].push_back(Expansion({rhsVals[3], rhsVals[4]}));
                    }
                }
            }
        } else {
            count += parseCFG(line, {0}, rules);
        }
    }

    return std::to_string(count);
}