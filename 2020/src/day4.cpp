#include "day4.hpp"
#include "util.hpp"
#include <algorithm>
#include <iostream>

/*
 * Passport Class
 */

// byr (Birth Year) - four digits; at least 1920 and at most 2002.
// iyr (Issue Year) - four digits; at least 2010 and at most 2020.
// eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
// hgt (Height) - a number followed by either cm or in:
// If cm, the number must be at least 150 and at most 193.
// If in, the number must be at least 59 and at most 76.
// hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
// ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
// pid (Passport ID) - a nine-digit number, including leading zeroes.
// cid (Country ID) - ignored, missing or not.
const std::map<std::string, std::regex> Passport::s_StrictRegex { 
  { "byr", std::regex("(19[2-9][0-9]|200[0-2])") }, 
  { "iyr", std::regex("20(1[0-9]|20)") },
  { "eyr", std::regex("20(2[0-9]|30)") },
  { "hgt", std::regex("((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)") },
  { "hcl", std::regex("#([0-9]|[a-f]){6}") },
  { "ecl", std::regex("(amb|blu|brn|gry|grn|hzl|oth)") },
  { "pid", std::regex("[0-9]{9}") },
  { "cid", std::regex(".*") }
};

void Passport::setField(std::string field, std::string value) {
    m_Details[field] = value;
}

bool Passport::isValid(bool strict) const {
    for(auto it = Passport::s_StrictRegex.begin(); it != Passport::s_StrictRegex.end(); ++it) {
        std::string fieldname = it->first;
        if(m_Details.find(fieldname) == m_Details.end()){
            if(fieldname != "cid")
                return false;
        } else if(strict){
            std::string value = m_Details.at(fieldname);
            std::regex regex = it->second;
            if(!std::regex_match(value, regex)){
                return false;
            }
        }
    }
    return true;
}

/*
 * Day 4 Class
 */
Day4::Day4() : Solver("day4") {}

std::vector<Passport> Day4::parseports(const std::vector<std::string>& input) {
    std::vector<Passport> list;
    Passport pass;
    for(std::string line : input) {
        if(line.empty()){
            list.push_back(pass);
            pass = Passport();
            continue;
        }
        
        std::vector<std::string> splitString = util::split(line, ' ');
        for(std::string token : splitString) {
            size_t pos = token.find(':');
            pass.setField(token.substr(0, pos), token.substr(pos+1));
        }
    }
    list.push_back(pass);
    return list;
}

std::string Day4::runPart1(const std::vector<std::string>& input) {
    std::vector<Passport> list = parseports(input);
    int countValid = std::count_if(list.begin(), list.end(), [](Passport const& p){
               return p.isValid();
            });
    return std::to_string(countValid);
}

std::string Day4::runPart2(const std::vector<std::string>& input) {
    std::vector<Passport> list = parseports(input);
    int countValid = std::count_if(list.begin(), list.end(), [](Passport const& p){
               return p.isValid(true);
            });
    return std::to_string(countValid);
}