#include "Solver.hpp"

class Day5 : public Solver {
public:
    Day5();
    std::string runPart1(const std::vector<std::string>& input) override;
    std::string runPart2(const std::vector<std::string>& input) override;
private:
    std::vector<std::pair<int, int>> parseSeats(const std::vector<std::string>& input);
};