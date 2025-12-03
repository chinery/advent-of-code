import Foundation

class Config {
    static let baseUrl = URL(fileURLWithPath: "/Users/andrew/dev/advent-of-code/2021/AoC2021/AoC2021/")
}

let start = ProcessInfo.processInfo.systemUptime

day13_1()

let end = ProcessInfo.processInfo.systemUptime

print()
print("Ran in \(Double(end - start)) seconds")
