#include "day16.hpp"
#include "util.hpp"
#include <set>

class Rule {
private:
    std::string m_Name;
    int m_Min1, m_Max1, m_Min2, m_Max2;
    std::set<int> m_ValidCols;
public:
    Rule(std::string name, int min1, int max1, int min2, int max2) 
        : m_Name(name), m_Min1(min1), m_Max1(max1), m_Min2(min2), m_Max2(max2) {}

    std::string getName() { return m_Name; }

    void initCols(int max) {
        for(int i = 0; i < max; i++){
            m_ValidCols.insert(i);
        }
    }

    void removeCol(int index){
        m_ValidCols.erase(index);
    }

    bool isValidCol(int index) {
        return m_ValidCols.find(index) != m_ValidCols.end();
    }

    int validColsCount() {
        return m_ValidCols.size();
    }

    int finalCol() {
        return *m_ValidCols.begin();
    }

    bool isValidValue(int value) {
        return (value >= m_Min1 && value <= m_Max1) || (value >= m_Min2 && value <= m_Max2);
    }
};

Day16::Day16() : Solver("day16") {}

std::string Day16::runPart1(const std::vector<std::string>& input) {
    int mode = 0;
    std::vector<Rule> rules;
    int sumInvalid = 0;
    for(auto& line : input) {
        if(mode == 0){
            // rules
            if(line == ""){
                mode++;
            } else {
                int r1 = line.find(':');
                rules.push_back(Rule(line.substr(0, r1),
                                     std::stoi(line.substr(r1+2, 2)),
                                     std::stoi(line.substr(r1+5, 3)),
                                     std::stoi(line.substr(r1+12, 3)),
                                     std::stoi(line.substr(r1+16, 3))));
            }
        } else if(mode == 1) {
            // your ticket
            if(line == ""){
                mode++;
            }
        } else {
            // nearby tickets
            if(line[0] != 'n') {
                std::vector<std::string> values = util::split(line, ',');
                for(auto& valStr : values){
                    int val = std::stoi(valStr);
                    bool anyRuleValid = false;
                    for(auto& rule : rules) {
                        if(rule.isValidValue(val)) {
                            anyRuleValid = true;
                            break;
                        }
                    }
                    if(!anyRuleValid){
                        sumInvalid += val;
                    }
                }
            }
        }
    }

    return std::to_string(sumInvalid);
}

// really messy, sorry if you're reading this...
std::string Day16::runPart2(const std::vector<std::string>& input) {
    int mode = 0;
    std::vector<Rule> rules;
    int sumInvalid = 0;
    std::vector<int> yourTicket;
    std::vector<std::vector<int>> validTickets;

    // parse the input and find valid tickets
    for(auto& line : input) {
        if(mode == 0){
            // rules
            if(line == ""){
                mode++;
            } else {
                int r1 = line.find(':');
                rules.push_back(Rule(line.substr(0, r1),
                                     std::stoi(line.substr(r1+2, 2)),
                                     std::stoi(line.substr(r1+5, 3)),
                                     std::stoi(line.substr(r1+12, 3)),
                                     std::stoi(line.substr(r1+16, 3))));
            }
        } else if(mode == 1) {
            // your ticket
            if(line == ""){
                mode++;
            } else if(line[0] != 'y') {
                yourTicket = util::split<int>(line, ',', [](std::string x)->int {return std::stoi(x);});
            }
        } else {
            // nearby tickets
            if(line[0] != 'n') {
                bool allRulesValid = true;
                std::vector<int> values = util::split<int>(line, ',', [](std::string x)->int {return std::stoi(x);});
                for(auto& val : values){
                    bool anyRuleValid = false;
                    for(auto& rule : rules) {
                        if(rule.isValidValue(val)) {
                            anyRuleValid = true;
                            break;
                        }
                    }
                    if(!anyRuleValid){
                        allRulesValid = false;
                        break;
                    }
                }
                if(allRulesValid) {
                    validTickets.push_back(values);
                }
            }
        }
    }

    // set each rule to contain each possible column index
    for(auto& rule : rules) rule.initCols(rules.size());

    // basic constraint propagation (AC-3) in spaghetti code
    //
    // for each rule, go through each value, and rule out columns
    // once a rule only has one possible column, update all other rules to remove this column
    std::set<std::string> finishedRules;
    while(finishedRules.size() < rules.size()) {
        for(auto& rule : rules){
            if(finishedRules.find(rule.getName()) != finishedRules.end()) {
                continue;
            }

            for(auto& ticketVals : validTickets) {
                for(int i = 0; i < ticketVals.size(); i++){
                    if(rule.isValidCol(i) && !rule.isValidValue(ticketVals[i])) {
                        rule.removeCol(i);
                        if(rule.validColsCount() == 1){
                            break;
                        }
                    }
                }
                if(rule.validColsCount() == 1){
                    break;
                }
            }

            if(rule.validColsCount() == 1){
                finishedRules.insert(rule.getName());
                for(auto& r : rules) {
                    if(r.validColsCount() > 1 && r.isValidCol(rule.finalCol())){
                        r.removeCol(rule.finalCol());
                    }
                }
            }
        }
    }

    long result = 1;
    for(auto& rule : rules){
        if(rule.getName().substr(0, 9) == "departure") {
            result *= yourTicket[rule.finalCol()];
        }
    }

    return std::to_string(result);
}