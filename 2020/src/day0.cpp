#include "day0.hpp"

namespace day0 {
    std::string runPart1(const std::vector<std::string> input) {
        long sum = 0;
        for(std::string line : input) {
            sum += (std::stoi(line) / 3) - 2;
        }
        return std::to_string(sum);
    }
}