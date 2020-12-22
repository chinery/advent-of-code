#include "day22.hpp"
#include <list>
#include <unordered_set>
#include <iostream>

Day22::Day22() : Solver("day22") {}

std::string Day22::runPart1(const std::vector<std::string>& input) {
    int player = 1;
    std::list<int> player1;
    std::list<int> player2;

    for(const auto& line : input){
        if(line == "Player 1:" || line == "") {
            continue;
        } else if(line == "Player 2:") {
            player++;
        } else if(player == 1){
            player1.push_back(std::stoi(line));
        } else {
            player2.push_back(std::stoi(line));
        }
    }

    while(player1.size() != 0 && player2.size() != 0) {
        if(player1.front() > player2.front()) {
            player1.push_back(player1.front());
            player1.push_back(player2.front());
        } else {
            player2.push_back(player2.front());
            player2.push_back(player1.front());
        }
        player1.pop_front();
        player2.pop_front();
    }

    std::list<int>* winner;
    if(player1.size() == 0) winner = &player2;
    else winner = &player1;

    long sum = 0;
    int i = 1;
    for(auto it = winner->rbegin(); it != winner->rend(); ++it){
        sum += *it * i++;
    }

    return std::to_string(sum);
}

int playGame(std::list<int> player1, std::list<int> player2, int game = 1) {
    std::unordered_set<std::string> player1prev;
    std::unordered_set<std::string> player2prev;

    auto l2str = [](const std::list<int>& l){ 
        std::string s;
        for (const auto &piece : l) s += (char)piece + ',';
        return s; 
    };

    while(player1.size() != 0 && player2.size() != 0) {
        auto p1str = l2str(player1);
        auto p2str = l2str(player2);

        if(player1prev.find(p1str) != player1prev.end() || player2prev.find(p2str) != player2prev.end()){
            return 1;
        } else {
            player1prev.insert(p1str);
            player2prev.insert(p2str);
        }

        int p1c = player1.front();
        int p2c = player2.front();
        player1.pop_front();
        player2.pop_front();

        int roundWin = 0;
        if(p1c <= player1.size() && p2c <= player2.size()) {
            roundWin = playGame(std::list<int>(player1.begin(), std::next(player1.begin(), p1c)),
                                std::list<int>(player2.begin(), std::next(player2.begin(), p2c)), game+1); 
        } else {
            roundWin = (p2c > p1c) + 1;
        }
        
        if(roundWin == 1) {
            player1.push_back(p1c);
            player1.push_back(p2c);
        } else {
            player2.push_back(p2c);
            player2.push_back(p1c);
        }
    }

    int winner = (player1.size() == 0) + 1;

    if(game == 1) {
        std::list<int>* winnerDeck;
        if(winner == 2) winnerDeck = &player2;
        else winnerDeck = &player1;

        int sum = 0;
        int i = 1;
        for(auto it = winnerDeck->rbegin(); it != winnerDeck->rend(); ++it){
            sum += *it * i++;
        }
        return sum;
    }

    return winner;
}

std::string Day22::runPart2(const std::vector<std::string>& input) {
    int player = 1;
    std::list<int> player1;
    std::list<int> player2;

    for(const auto& line : input){
        if(line == "Player 1:" || line == "") {
            continue;
        } else if(line == "Player 2:") {
            player++;
        } else if(player == 1){
            player1.push_back(std::stoi(line));
        } else {
            player2.push_back(std::stoi(line));
        }
    }

    int sum = playGame(player1, player2, 1);

    return std::to_string(sum);
}