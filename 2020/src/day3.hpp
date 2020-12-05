#include "Solver.hpp"

class Day3 : public Solver {
public:
    Day3();
    std::string runPart1(const std::vector<std::string>& input) override;
    std::string runPart2(const std::vector<std::string>& input) override;
private:
    int countTrees(const std::vector<std::string>& input, int moveDown, int moveRight);
};