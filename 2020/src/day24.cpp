#include "day24.hpp"
#include <unordered_set>
#include <iostream>

struct HexPoint { 
    int x, y, z; 

    HexPoint(int x=0, int y=0) 
        : x(x), y(y)
    {}
    
    HexPoint& operator+=(const HexPoint& rhs) {
        x += rhs.x; y += rhs.y;
        return *this;
    }

    HexPoint& operator-=(const HexPoint& rhs) {
        x -= rhs.x; y -= rhs.y;
        return *this;
    }
        
    HexPoint& operator*=(const int rhs) {
        x *= rhs; y *= rhs;
        return *this;
    }

    bool operator==(const HexPoint& rhs) const {
        return x == rhs.x && y == rhs.y;
    }
};

HexPoint operator+(HexPoint lhs, const HexPoint& rhs) {
    return lhs += rhs;
}

HexPoint operator-(HexPoint lhs, const HexPoint& rhs) {
    return lhs -= rhs;
}

HexPoint operator*(HexPoint lhs, const int rhs) {
    return lhs *= rhs;
}

namespace std {
    template<> struct hash<HexPoint> {
        std::size_t operator()(const HexPoint& p) const noexcept {
            return (p.x * 31) + (p.y * 37);
        }
    };
}

const static HexPoint E = {1, 0}, NE = {0, 1}, NW = {-1, 1}, W={-1, 0}, SW = {0, -1}, SE = {1, -1}, NONE = {0, 0};

Day24::Day24() : Solver("day24") {}

std::string Day24::runPart1(const std::vector<std::string>& input) {
    std::unordered_set<HexPoint> flipped; 
    int count = 0;
    
    for(auto& line : input) {
        int i = 0;
        HexPoint flipPt;
        while(i < line.length()){
            if(line[i] == 'e') {
                flipPt += E;
                i++;
            } else if(line[i] == 'w') {
                flipPt += W;
                i++;
            } else if(line[i] == 'n') {
                if(line[i+1] == 'e') {
                    flipPt += NE;
                } else { // 'nw'
                    flipPt += NW;
                }
                i += 2;
            } else { // 's'
                if(line[i+1] == 'e') {
                    flipPt += SE;
                } else { // 'sw'
                    flipPt += SW;
                }
                i += 2;
            }
        }
        
        if(flipped.find(flipPt) == flipped.end()) {
            count++;
            flipped.insert(flipPt);
        } else {
            count--;
            flipped.erase(flipPt);
        }
    }

    return std::to_string(count);
}

std::string Day24::runPart2(const std::vector<std::string>& input) {
    std::unordered_set<HexPoint> flipped; 

    int count = 0;
    
    for(auto& line : input) {
        int i = 0;
        HexPoint flipPt;
        while(i < line.length()){
            if(line[i] == 'e') {
                flipPt += E;
                i++;
            } else if(line[i] == 'w') {
                flipPt += W;
                i++;
            } else if(line[i] == 'n') {
                if(line[i+1] == 'e') {
                    flipPt += NE;
                } else { // 'nw'
                    flipPt += NW;
                }
                i += 2;
            } else { // 's'
                if(line[i+1] == 'e') {
                    flipPt += SE;
                } else { // 'sw'
                    flipPt += SW;
                }
                i += 2;
            }
        }
        
        if(flipped.find(flipPt) == flipped.end()) {
            flipped.insert(flipPt);
            count++;
        } else {
            flipped.erase(flipPt);
            count--;
        }
    }

    for(int round = 1; round <= 100; round++){
        std::unordered_set<HexPoint> oldGrid(flipped); 
        std::unordered_set<HexPoint> checked;

        for(const HexPoint& point : oldGrid) {
            for(const HexPoint& dir : {NW, NE, E, SE, SW, W, NONE}) {
                HexPoint ptr = point + dir;

                if(checked.find(ptr) != checked.end()) continue;

                bool tileBlack = oldGrid.find(ptr) != oldGrid.end();
                
                int countAdj = 0;
                for(const HexPoint& sdir : {NW, NE, E, SE, SW, W}) {
                    if(oldGrid.find(ptr + sdir) != oldGrid.end()) countAdj++;
                }

                if(tileBlack && (countAdj == 0 || countAdj > 2)) {
                    flipped.erase(ptr);
                    count--;
                } else if(!tileBlack && countAdj == 2) {
                    flipped.insert(ptr);
                    count++;
                }

                checked.insert(ptr);
            }
        }

        oldGrid = flipped;
    }

    return std::to_string(count);
}