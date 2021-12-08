import Foundation

private func getInput(file: String) -> [Int] {
    let baseUrl = URL(fileURLWithPath: "/Users/andrew/dev/advent-of-code/2021/AoC2021/AoC2021/Day 1/")
    let url = baseUrl.appendingPathComponent(file)
    let strings = Utils.readLines(url: url)
    
    return strings.map {Int($0)!}
}

func day1_1() {
    let integers = getInput(file: "input.txt")
    
    let count = zip(integers.prefix(upTo: integers.count - 1),
                    integers.suffix(from: 1))
        .map {$0.1 - $0.0}
        .filter {$0 > 0}
        .count
    
    print(count)
}

func day1_2() {
    let integers = getInput(file: "input.txt")
    
    let sums = zip(integers[0 ..< integers.count - 2],
                       zip(integers[1 ..< integers.count - 1],
                           integers[2 ..< integers.count]))
                .map {$0.0 + $0.1.0 + $0.1.1}
    
    let count = zip(sums.prefix(upTo: sums.count - 1),
                    sums.suffix(from: 1))
        .map {$0.1 - $0.0}
        .filter {$0 > 0}
        .count
    
    print(count)
}
