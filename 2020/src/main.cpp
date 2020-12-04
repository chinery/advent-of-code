#include <iostream>
#include <vector>
#include <string>

#include "day4.hpp"

int main()
{
	Solver* solver = new Day4();
    std::vector<std::string> input = solver->getInput();
    std::cout << solver->runPart1(input) << std::endl;
	std::cout << solver->runPart2(input) << std::endl;
	delete solver;
	return 0;
}