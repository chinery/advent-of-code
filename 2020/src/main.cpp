#include <iostream>
#include <vector>
#include <string>

#include "day9.hpp"

int main()
{
	Solver* solver = new Day9();
    std::vector<std::string> input = solver->getInput();
    std::cout << solver->runPart1(input) << std::endl;
	std::cout << solver->runPart2(input) << std::endl;
	delete solver;
	return 0;
}