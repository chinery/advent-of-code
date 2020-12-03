#include "Solver.hpp"
#include <iostream>
#include <fstream>

Solver::Solver(std::string file): m_File(file) {}

std::vector<std::string> Solver::getInput() {
    std::string filename = "../data/" + m_File + ".txt";
    std::ifstream myFile(filename);

	std::vector<std::string> input;
	std::string line;
	while (std::getline(myFile, line))
	{
		input.push_back(line);
	}
	return input;
}