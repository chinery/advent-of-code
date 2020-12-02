#include <iostream>
#include <vector>
#include <string>
#include <fstream>

#include "day2.hpp"
using namespace day2;
static const std::string filename = "../data/day2.txt";

std::vector<std::string> get_input(const std::string& filename)
{
    std::ifstream myFile(filename);

	std::vector<std::string> input;
	std::string line;
	while (std::getline(myFile, line))
	{
		input.push_back(line);
	}
	return input;
}

int main()
{
    std::vector input = get_input(filename);
    std::cout << runPart1(input) << std::endl;
	// std::cout << runPart2(input) << std::endl;
}