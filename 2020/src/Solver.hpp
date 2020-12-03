#pragma once

#include <string>
#include <vector>

class Solver {
private:
    std::string m_File;
public:
    Solver(std::string file);
    virtual ~Solver() {}
    std::vector<std::string> getInput();
    virtual std::string runPart1(const std::vector<std::string>& input) = 0;
    virtual std::string runPart2(const std::vector<std::string>& input) = 0;
};

