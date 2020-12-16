#pragma once
#include <string>
#include <vector>

namespace util {
    // https://stackoverflow.com/a/7408245 (see .cpp)
    std::vector<std::string> split(const std::string &text, char sep = ' ');

    // modified from the above
    template <typename T>
    std::vector<T> split(const std::string &text, char sep, std::function<T(std::string)> convertFn) {
        std::vector<T> tokens;
        std::size_t start = 0, end = 0;
        while ((end = text.find(sep, start)) != std::string::npos) {
            tokens.push_back(convertFn(text.substr(start, end - start)));
            start = end + 1;
        }
        tokens.push_back(convertFn(text.substr(start)));
        return tokens;
    }
}