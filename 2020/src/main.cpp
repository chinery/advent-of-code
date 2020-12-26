#include <iostream>
#include <vector>
#include <string>
#include <chrono>

#include "day25.hpp"

int main()
{
	Solver* solver = new Day25();
    std::vector<std::string> input = solver->getInput();
	auto start = std::chrono::high_resolution_clock::now();

    std::cout << solver->runPart1(input) << std::endl;
	std::cout << solver->runPart2(input) << std::endl;
	
	auto finish = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> elapsed = finish - start;
	std::cout << "Elapsed time: " << elapsed.count() << " s" << std::endl;

	delete solver;
	return 0;
}