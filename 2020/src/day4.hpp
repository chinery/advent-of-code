#include "Solver.hpp"
#include <map>
#include <regex>

class Passport {
private:
    std::map<std::string, std::string> m_Details;
    static const std::map<std::string, std::regex> s_StrictRegex;
public:
    void setField(std::string field, std::string value);
    bool isValid(bool strict = false) const;
};

class Day4 : public Solver {
public:
    Day4();
    std::string runPart1 (const std::vector<std::string>& input) override;
    std::string runPart2(const std::vector<std::string>& input) override;
private:
    void parseports(const std::vector<std::string>& input, std::vector<Passport>& list);
};

