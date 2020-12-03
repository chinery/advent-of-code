#include <iostream>
#include <vector>
#include <string>

#include "day3.hpp"

int main()
{
	Solver* solver = new Day3();
    std::vector<std::string> input = solver->getInput();
    std::cout << solver->runPart1(input) << std::endl;
	std::cout << solver->runPart2(input) << std::endl;
	delete solver;
	return 0;
}