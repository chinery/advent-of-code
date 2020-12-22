#include "day20.hpp"
#include <unordered_map>
#include <unordered_set>
#include <iostream>

std::string reversed(std::string &sin) {
    std::string s(sin);
    std::reverse(s.begin(), s.end());
    return s;
}

void reverse(std::string &s) {
    std::reverse(s.begin(), s.end());
}

class Tile {
private:
    int id;
    std::string up, down, left, right;
    std::vector<std::string> contents;
    static std::unordered_map<std::string, std::vector<int>> sidesToID;
public:
    Tile(int id, const std::string& up, const std::string& right, const std::string& down, const std::string& left) {
        this->id = id;
        this->up = up;
        this->down = down;
        this->left = left;
        this->right = right;

        sidesToID[this->up].push_back(id);
        sidesToID[reversed(this->up)].push_back(id);
        sidesToID[this->down].push_back(id);
        sidesToID[reversed(this->down)].push_back(id);
        sidesToID[this->left].push_back(id);
        sidesToID[reversed(this->left)].push_back(id);
        sidesToID[this->right].push_back(id);
        sidesToID[reversed(this->right)].push_back(id);
    }

    Tile(int id, const std::string& up, const std::string& right, const std::string& down, const std::string& left, std::vector<std::string> contents) {
        this->id = id;
        this->up = up;
        this->down = down;
        this->left = left;
        this->right = right;

        sidesToID[this->up].push_back(id);
        sidesToID[reversed(this->up)].push_back(id);
        sidesToID[this->down].push_back(id);
        sidesToID[reversed(this->down)].push_back(id);
        sidesToID[this->left].push_back(id);
        sidesToID[reversed(this->left)].push_back(id);
        sidesToID[this->right].push_back(id);
        sidesToID[reversed(this->right)].push_back(id);

        this->contents = contents;
    }

    static void clear() {
        sidesToID.clear();
    }

    int getID() const {
        return id;
    }

    bool isCorner() const {
        int sharedEdge = 0;
        if(sidesToID[this->up].size() > 1) sharedEdge++;
        if(sidesToID[this->down].size() > 1) sharedEdge++;
        if(sidesToID[this->left].size() > 1) sharedEdge++;
        if(sidesToID[this->right].size() > 1) sharedEdge++;
        // std::cout << id << ": " << sidesToID[this->up].size() << ',' << sidesToID[this->down].size() << ',' << sidesToID[this->left].size() << ',' << sidesToID[this->right].size() << std::endl;
        return sharedEdge == 2;
    }

    bool isCornerOrEdge() const {
        int sharedEdge = 0;
        if(sidesToID[this->up].size() > 1) sharedEdge++;
        if(sidesToID[this->down].size() > 1) sharedEdge++;
        if(sidesToID[this->left].size() > 1) sharedEdge++;
        if(sidesToID[this->right].size() > 1) sharedEdge++;
        return sharedEdge == 2 || sharedEdge == 3;
    }

    void rotate90cw() {
        auto temp = up;
        up = reversed(left);
        left = down;
        down = reversed(right);
        right = temp;

        std::vector<std::string> newContents;
        for(int j = 0; j < contents[0].length(); j++) {
            std::string line = "";
            for(int i = contents.size() - 1; i >= 0; i--) {
                line += contents[i][j];
            }
            newContents.push_back(line);
        }
        contents = newContents;
    }

    void rotate180() {
        auto temp = up;
        up = reversed(down);
        down = reversed(up);
        temp = left;
        left = reversed(right);
        right = reversed(temp);

        for(auto& line : contents){
            reverse(line);
        }
        std::reverse(this->contents.begin(), this->contents.end());

    }

    void rotate270cw() {
        auto temp = up;
        up = right;
        right = reversed(down);
        down = left;
        left = reversed(temp);

        std::vector<std::string> newContents;
        for(int j = contents[0].length() - 1; j >= 0; j--) {
            std::string line = "";
            for(int i = 0; i < contents.size(); i++) {
                line += contents[i][j];
            }
            newContents.push_back(line);
        }
        contents = newContents;
    }

    void flipLR(){
        auto temp = left;
        left = right;
        right = temp;

        reverse(up);
        reverse(down);

        for(auto& line : contents){
            reverse(line);
        }
    }

    void flipUD(){
        auto temp = up;
        up = down;
        down = temp;

        reverse(left);
        reverse(right);

        std::reverse(this->contents.begin(), this->contents.end());
    }

    static std::vector<std::string> orient(std::unordered_map<int, Tile>& tiles, std::unordered_set<int> edgeCornerIDs, std::unordered_set<int> cornerIDs) {
        // initialise 8 empty strings which will contain 8 rows
        std::string rowBlock[8];
        std::vector<std::string> result;

        // find the top left corner
        int tlCornerId = -1;
        for(auto& pair : tiles) {
            if(cornerIDs.find(pair.first) != cornerIDs.end()) {
                if(sidesToID[pair.second.up].size() == 1 && sidesToID[pair.second.left].size() == 1) {
                    tlCornerId = pair.first;
                    break;
                }
            }
        }

        if(tlCornerId == -1) std::cerr << "No top left corner found" << std::endl;

        int row = 0, col = 0;

        Tile* topLeft = &tiles.find(tlCornerId)->second;
        Tile* startRow = topLeft;
        Tile* prev = startRow;
        bool finalRow = false;

        while(!finalRow) {
            ++row;

            for(int i = 0; i < 8; i++){
                rowBlock[i] = startRow->contents[i];
            }

            if(startRow != topLeft && cornerIDs.find(startRow->getID()) != cornerIDs.end()) {
                finalRow = true;
            }

            Tile* ptr = startRow;
            prev = ptr;

            std::cout << startRow->id << '-';
            
            col = 0;
            // go right until corner or edge
            while(ptr==prev
                  || ((finalRow || startRow == topLeft) && cornerIDs.find(ptr->getID()) == cornerIDs.end())
                  || edgeCornerIDs.find(ptr->getID()) == edgeCornerIDs.end()) {
                
                ++col;

                int rightId;
                if(sidesToID[ptr->right][0] == ptr->id) rightId = sidesToID[ptr->right][1];
                else rightId = sidesToID[ptr->right][0];

                prev = ptr;
                ptr = &tiles.find(rightId)->second;

                std::cout << ptr->id << '-';
                
                if(ptr->left == prev->right){
                    // do nothing
                } else if(ptr->down == prev->right) {
                    ptr->rotate90cw();
                    assert(ptr->left == prev->right);
                } else if(ptr->right == prev->right) {
                    ptr->flipLR();
                    assert(ptr->left == prev->right);
                } else if(ptr->up == prev->right) {
                    ptr->rotate270cw();
                    ptr->flipUD();
                    assert(ptr->left == prev->right);
                } else if(reversed(ptr->left) == prev->right) {
                    ptr->flipUD();
                    assert(ptr->left == prev->right);
                } else if(reversed(ptr->down) == prev->right) {
                    ptr->rotate90cw();
                    ptr->flipUD();
                    assert(ptr->left == prev->right);
                } else if(reversed(ptr->right) == prev->right) {
                    ptr->rotate180();
                    assert(ptr->left == prev->right);
                } else if(reversed(ptr->up) == prev->right) {
                    ptr->rotate270cw();
                    assert(ptr->left == prev->right);
                } else {
                    std::cerr << "Oh no! Sides don't match??" << std::endl;
                }
                assert(ptr->left == prev->right);

                for(int i = 0; i < 8; i++){
                    rowBlock[i] += ptr->contents[i];
                }
            } // end while(ptr==prev || !ptr->isCornerOrEdge())

            std::cout << std::endl;

            for(int i = 0; i < 8; i++) {
                result.push_back(rowBlock[i]);
                // std::cout << rowBlock[i] << std::endl;
            }

            if(finalRow) {
                break;
            }

            // go down one
            int downId; 
            if(sidesToID[startRow->down][0] == startRow->id) downId = sidesToID[startRow->down][1];
            else downId = sidesToID[startRow->down][0];

            prev = startRow;
            startRow = &tiles.find(downId)->second;
            
            if(startRow->up == prev->down){
                // do nothing
            } else if(startRow->left == prev->down) {
                startRow->rotate90cw();
                startRow->flipLR();
                assert(startRow->up == prev->down);
            } else if(startRow->down == prev->down) {
                startRow->flipUD();
                assert(startRow->up == prev->down);
            } else if(startRow->right == prev->down) {
                startRow->rotate270cw();
                assert(startRow->up == prev->down);
            } else if(reversed(startRow->up) == prev->down) {
                startRow->flipLR();
                assert(startRow->up == prev->down);
            } else if(reversed(startRow->left) == prev->down) {
                startRow->rotate90cw();
                assert(startRow->up == prev->down);
            } else if(reversed(startRow->down) == prev->down) {
                startRow->rotate180();
                assert(startRow->up == prev->down);
            } else if(reversed(startRow->right) == prev->down) {
                startRow->rotate270cw();
                startRow->flipLR();
                assert(startRow->up == prev->down);
            } else {
                std::cerr << "Oh no! Sides don't match??" << std::endl;
            }
            assert(startRow->up == prev->down);
        }

        return result;
    }
};

std::unordered_map<std::string, std::vector<int>> Tile::sidesToID;

Day20::Day20() : Solver("day20") {}

std::string Day20::runPart1(const std::vector<std::string>& input) {
    std::vector<Tile> tiles;
    int id;
    std::string left, right, up, down;
    for(const auto& line : input){
        if(line[0] == 'T') {
            id = std::stoi(line.substr(5, 4));
        } else if(line == ""){
            left = "";
            right = "";
            continue;
        } else if(left.length() == 9) {
            down = line;
            left += line[0];
            right += line[9];
            Tile t(id, up, right, down, left);
            tiles.push_back(t);
        } else if(left.length() == 0) {
            up = line;
            left += line[0];
            right += line[9];
        } else {
            left += line[0];
            right += line[9];
        }
    }

    long mult = 1;
    for(const auto& tile : tiles) {
        if(tile.isCorner()) {
            mult *= tile.getID();
            // std::cout << tile.getID() << std::endl;
        }
    }

    return std::to_string(mult);
}

struct Point {int row, col;};
bool operator==(Point a, Point b) { return a.row==b.row && a.col==b.col; }

std::string Day20::runPart2(const std::vector<std::string>& input) {
    Tile::clear(); // need to clear static map if running part 1 first

    std::unordered_map<int, Tile> tiles;
    int id;
    std::string left, right, up, down;
    std::vector<std::string> contents;
    for(const auto& line : input){
        if(line[0] == 'T') {
            id = std::stoi(line.substr(5, 4));
        } else if(line == ""){
            left = "";
            right = "";
            contents.clear();
            continue;
        } else if(left.length() == 9) {
            down = line;
            left += line[0];
            right += line[9];
            tiles.insert({id, Tile(id, up, right, down, left, contents)});
        } else if(left.length() == 0) {
            up = line;
            left += line[0];
            right += line[9];
        } else {
            left += line[0];
            right += line[9];
            contents.push_back(line.substr(1, 8));
        }
    }

    std::unordered_set<int> edgeCornerIDs;
    std::unordered_set<int> cornerIDs;

    for(const auto& pair : tiles) {
        if(pair.second.isCornerOrEdge()) {
            edgeCornerIDs.insert(pair.second.getID());
            if(pair.second.isCorner()){
                cornerIDs.insert(pair.second.getID());
            }
        }
    }

    auto picture = Tile::orient(tiles, edgeCornerIDs, cornerIDs);


    // std::reverse(picture.begin(), picture.end());


    int countwave = 0;
    for(int i = 0; i < picture.size(); i++){
        if(i%8 == 0) std::cout << std::endl;
        for(int j = 0; j < picture[0].length(); j++) {
            if(j%8 == 0) std::cout << ' ';
            if(picture[i][j] == '#') {
                countwave++;
                std::cout << '#';
            } else {
                std::cout << '.';
            }
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
    std::cout << std::endl;

    std::vector<std::string> monster = {"                  # ",
                                        "#    ##    ##    ###",
                                        " #  #  #  #  #  #   "};

    std::vector<std::vector<Point>> all_mpoints(8, std::vector<Point>());

    for(int i = 0; i < 3; i++){
        for(int j = 0; j < monster[0].length(); j++) {
            if(monster[i][j] == '#') {
                all_mpoints[0].push_back({i, j});
                all_mpoints[1].push_back({j, i});
                all_mpoints[2].push_back({-i + 2, j});
                all_mpoints[3].push_back({j, -i + 2});
                all_mpoints[4].push_back({i, -j + 19});
                all_mpoints[5].push_back({-j + 19, i});
                all_mpoints[6].push_back({-i + 2, -j + 19});
                all_mpoints[7].push_back({-j + 19, -i + 2});
            }
        }
    }

    for(auto& mpoints : all_mpoints) {
        int countmonster = 0;

        int maxi = 0, maxj = 0;
        for(auto& point : mpoints){
            if(point.row > maxi) maxi = point.row;
            if(point.col > maxj) maxj = point.col;
        }

        for(int i = 0; i < maxi+1; i++) {
            for(int j = 0; j < maxj+1; j++) {
                if(std::find(mpoints.begin(), mpoints.end(), (Point){i, j}) != mpoints.end()) {
                    std::cout << 'X';
                } else {
                    std::cout << '.';
                }
            }
            std::cout << std::endl;
        }

        std::cout << std::endl;
        std::cout << std::endl;

        for(int i = 0; i < picture.size() - maxi; i++){
            for(int j = 0; j < picture[0].length() - maxj; j++) {
                bool found = true;
                for(auto& point : mpoints){
                    if(picture[i + point.row][j + point.col] != '#') {
                        found = false;
                        break;
                    }
                }
                if(found) {
                    countmonster++;
                    countwave -= mpoints.size();
                }
            }
        }

        if(countmonster > 0){
            std::cout << "countmonster " << countmonster << std::endl;
            return std::to_string(countwave);
        }
    }

    return "welp";
}