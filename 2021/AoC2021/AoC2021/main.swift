import Foundation

class Config {
    static let baseUrl = URL(fileURLWithPath: "/Users/andrew/dev/advent-of-code/2021/AoC2021/AoC2021/")
}

let start = mach_absolute_time()

day3_2()

let end = mach_absolute_time()

print()
print("Ran in \(Double(end - start) / Double(NSEC_PER_SEC)) seconds")
