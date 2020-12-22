#include "Solver.hpp"
#include <iostream>
#include <fstream>
#include <filesystem>

Solver::Solver(std::string file): m_File(file) {}

std::vector<std::string> Solver::getInput() {
    std::string filename = "/data/" + m_File + ".txt";
	std::string path = std::filesystem::current_path();
    std::ifstream myFile(path + filename);

	std::vector<std::string> input;
	std::string line;
	while (std::getline(myFile, line))
	{
		input.push_back(line);
	}
	return input;
}