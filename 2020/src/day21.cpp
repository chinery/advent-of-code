#include "day21.hpp"
#include "util.hpp"
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <iostream>

Day21::Day21() : Solver("day21") {}

std::string Day21::runPart1(const std::vector<std::string>& input) {
    std::unordered_map<std::string, std::unordered_set<std::string>> allergenWordOptions;
    std::unordered_map<std::string, int> allWords;
    for(const auto& line : input) {
        std::vector<std::string> words = util::split(line, ' ');
        int mode = 0;
        std::unordered_set<std::string> thisLineWords;
        for(auto it = words.begin(); it != words.end(); ++it) {
            if(*it == "(contains") mode++;
            else if(mode == 0) {
                // other language words
                thisLineWords.insert(*it);
                allWords[*it]++;
            } else {
                // allergens
                // note: remove the final ')' or ','
                std::string allergen = (*it).substr(0, (*it).length() - 1);

                if(allergenWordOptions.find(allergen) == allergenWordOptions.end()) {
                    allergenWordOptions[allergen].insert(thisLineWords.begin(), thisLineWords.end());
                } else {
                    for(auto wordit = allergenWordOptions[allergen].begin(); wordit != allergenWordOptions[allergen].end();) {
                        if(thisLineWords.find(*wordit) == thisLineWords.end()) {
                            wordit = allergenWordOptions[allergen].erase(wordit);
                        } else{
                            ++wordit;
                        }
                    }
                }
            }
        }
    }
    int sum = 0;
    for(const auto& wordCountPair : allWords) {
        bool possible = false;
        for(const auto& allergenSetPair : allergenWordOptions) {
            if(allergenSetPair.second.find(wordCountPair.first) != allergenSetPair.second.end()) {
                possible = true;
                break;
            }
        }
        if(!possible) sum += wordCountPair.second;
    }

    return std::to_string(sum);
}

std::string Day21::runPart2(const std::vector<std::string>& input) {
    std::map<std::string, std::unordered_set<std::string>> allergenWordOptions;
    std::unordered_map<std::string, int> allWords;
    for(const auto& line : input) {
        std::vector<std::string> words = util::split(line, ' ');
        int mode = 0;
        std::unordered_set<std::string> thisLineWords;
        for(auto it = words.begin(); it != words.end(); ++it) {
            if(*it == "(contains") mode++;
            else if(mode == 0) {
                // other language words
                thisLineWords.insert(*it);
                allWords[*it]++;
            } else {
                // allergens
                // note: remove the final ')' or ','
                std::string allergen = (*it).substr(0, (*it).length() - 1);

                if(allergenWordOptions.find(allergen) == allergenWordOptions.end()) {
                    allergenWordOptions[allergen].insert(thisLineWords.begin(), thisLineWords.end());
                } else {
                    for(auto wordit = allergenWordOptions[allergen].begin(); wordit != allergenWordOptions[allergen].end();) {
                        if(thisLineWords.find(*wordit) == thisLineWords.end()) {
                            wordit = allergenWordOptions[allergen].erase(wordit);
                        } else{
                            ++wordit;
                        }
                    }
                }
            }
        }
    }

    std::string out = "";

    bool done = false;
    while(!done) { 
        done = true;
        for(auto& allergenSetPair : allergenWordOptions) {
            if(allergenSetPair.second.size() == 1) {
                for(auto& innerPair : allergenWordOptions) {
                    if(innerPair.second.size() > 1 && innerPair != allergenSetPair) {
                        innerPair.second.erase(*(allergenSetPair.second.begin()));
                        done = false;
                    }
                }
            }
        }
    }

    for(auto& allergenSetPair : allergenWordOptions) {
        out += *allergenSetPair.second.begin() + ',';
    }

    return out.substr(0, out.length() - 1);
}