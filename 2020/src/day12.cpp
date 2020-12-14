#include "day12.hpp"

Day12::Day12() : Solver("day12") {}

class Ship {
private:
    const static char s_Directions[4];
    int m_Direction = 0;
    int x = 0, y = 0;
public:
    void processCommand(char command, int value);

    int manhattanDistance();
};

const char Ship::s_Directions[4] = {'E', 'S', 'W', 'N'};

void Ship::processCommand(char command, int value) {
    if(command == 'F') command = s_Directions[m_Direction];
    switch(command) {
        case 'N':
            y += value;
            break;
        case 'S':
            y -= value;
            break;
        case 'E':
            x += value;
            break;
        case 'W':
            x -= value;
            break;
        case 'R':
            m_Direction = (m_Direction + (value / 90)) % 4;
            break;
        case 'L':
            m_Direction = m_Direction - (value / 90);
            if(m_Direction < 0) m_Direction += 4;
            break;
    }
}

int Ship::manhattanDistance() {
    return abs(x) + abs(y);
}

std::string Day12::runPart1(const std::vector<std::string>& input) {
    Ship ship;
    for(const std::string& line : input) {
        ship.processCommand(line[0], std::stoi(line.substr(1)));
    }

    return std::to_string(ship.manhattanDistance());
}

class Ship2 {
private:
    const static char s_Directions[4];
    int m_Direction = 0;
    long x = 0, y = 0;
    long w_x = 10, w_y = 1;
public:
    void processCommand(char command, int value);

    long manhattanDistance();
};

void Ship2::processCommand(char command, int value) {
    switch(command) {
        case 'N':
            w_y += value;
            break;
        case 'S':
            w_y -= value;
            break;
        case 'E':
            w_x += value;
            break;
        case 'W':
            w_x -= value;
            break;
        case 'F':
            x += value*w_x;
            y += value*w_y;
            break;
        case 'R':
            if(value == 90) {
                value = 270;
            }
            else if(value == 270) {
                value = 90;
            }
        case 'L':
            int temp_x = w_x;
            int temp_y = w_y;
            if(value == 90){
                w_x = -1 * temp_y;
                w_y = temp_x;
            } else if(value == 180) {
                w_x = -1 * temp_x;
                w_y = -1 * temp_y;
            } else {
                w_x = temp_y;
                w_y = -1 * temp_x;
            }
            break;
    }
}

long Ship2::manhattanDistance() {
    return abs(x) + abs(y);
}

std::string Day12::runPart2(const std::vector<std::string>& input) {
    Ship2 ship;
    for(const std::string& line : input) {
        ship.processCommand(line[0], std::stoi(line.substr(1)));
    }

    return std::to_string(ship.manhattanDistance());
}