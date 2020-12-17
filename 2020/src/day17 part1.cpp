// #include "day17.hpp"
// #include <unordered_set>
// #include <iostream>

// struct Point {
//     int x, y, z;

//     bool operator==(const Point& rhs) const {
//         return x == rhs.x && y == rhs.y && z == rhs.z;
//     }
// };

// namespace std {
//     template<> struct hash<Point>
//     {
//         std::size_t operator()(const Point& p) const noexcept
//         {
//             return (p.x * 31) + (p.y * 37) + (p.z * 41);
//         }
//     };
// }

// class PocketDimension {
// private:
//     std::unordered_set<Point> m_CellActive;
//     int m_Age = 0;
// public:
//     PocketDimension() = default;

//     PocketDimension (const PocketDimension &old_obj) {
//         m_CellActive = old_obj.m_CellActive;
//         m_Age = old_obj.m_Age;
//     } 

//     void set(int x, int y, int z, bool value) {
//         if(value) {
//             m_CellActive.insert({x, y, z});
//         } else {
//             m_CellActive.erase({x, y, z});
//         }
//     }

//     bool get(int x, int y, int z) {
//         if(m_CellActive.find({x, y, z}) != m_CellActive.end()) {
//             return true;
//         }
//         return false;
//     }

//     int getAge() {
//         return m_Age;
//     }

//     std::pair<Point, Point> getMinMax() {
//         Point min = *m_CellActive.begin();
//         Point max = *m_CellActive.begin();

//         for(const Point& point : m_CellActive) {
//             if(point.x < min.x) min.x = point.x;
//             if(point.y < min.y) min.y = point.y;
//             if(point.z < min.z) min.z = point.z;
//             if(point.x > max.x) max.x = point.x;
//             if(point.y > max.y) max.y = point.y;
//             if(point.z > max.z) max.z = point.z;
//         }

//         return {min, max};
//     }

//     int countNeighbours(int x, int y, int z) {
//         int count = 0;
//         for(int i = x-1; i <= x+1; i++) {
//             for(int j = y-1; j <= y+1; j++) {
//                 for(int k = z-1; k <= z+1; k++) {
//                     if(get(i, j, k)) count++;
//                 }
//             }   
//         }
//         if(get(x, y, z)) count--;
//         return count;
//     }

//     int advance() {
//         PocketDimension old(*this);

//         // look at this cool C++17 syntax
//         auto [min, max] = old.getMinMax();

//         --min.x; --min.y; --min.z;
//         ++max.x; ++max.y; ++max.z;

//         for(int i = min.x; i <= max.x; i++){
//             for(int j = min.y; j <= max.y; j++){
//                 for(int k = min.z; k <= max.z; k++){
//                     int count = old.countNeighbours(i, j, k);
//                     if(old.get(i, j, k) && count != 2 && count != 3) {
//                         this->set(i, j, k, false);
//                     } else if(!old.get(i, j, k) && count == 3){
//                         this->set(i, j, k, true);
//                     }
//                 }
//             }
//         }

//         this->m_Age++;
//         return this->m_CellActive.size();
//     }

//     void print() {
//         auto [min, max] = getMinMax();

//         --min.x; --min.y; --min.z;
//         ++max.x; ++max.y; ++max.z;

//         for(int k = min.z; k <= max.z; k++){
//             for(int i = min.x; i <= max.x; i++){
//                 for(int j = min.y; j <= max.y; j++){
//                     if(get(i, j, k)) {
//                         std::cout << '#';
//                     } else {
//                         std::cout << '.';
//                     }
//                 }
//                 std::cout << std::endl;
//             }
//             std::cout << std::endl;
//             std::cout << std::endl;
//         }
//     }

// };

// Day17::Day17() : Solver("day17") {}

// std::string Day17::runPart1(const std::vector<std::string>& input) {
//     PocketDimension pd;
//     for(int i = 0; i < input.size(); i++){
//         for(int j = 0; j < input[0].size(); j++) {
//             if(input[i][j] == '#') {
//                 pd.set(i, j, 0, true);
//             }
//         }
//     }

//     int count = 0;
//     // pd.print();
//     while(pd.getAge() < 6) {
//         count = pd.advance();
//         // pd.print();
//     }
//     return std::to_string(count);
// }

// std::string Day17::runPart2(const std::vector<std::string>& input) {
//     return "";
// }