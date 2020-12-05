#include "Solver.hpp"

class Day2 : public Solver {
public:
    Day2();
    std::string runPart1(const std::vector<std::string>& input) override;
    std::string runPart2(const std::vector<std::string>& input) override;
private:
    int processAndCount(const std::vector<std::string>& input, int part);
};