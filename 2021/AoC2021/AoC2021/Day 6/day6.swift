import Foundation
import Collections


private func getInput(file: String = "input.txt") -> [Int] {
    let url = Config.baseUrl.appendingPathComponent("Day 6/").appendingPathComponent(file)
    let strings = Utils.readLines(url: url)
    
    
    return strings[0].split(separator: ",").map {Int($0)!}
}

func day6_1() {
    let numbers = getInput()
    
    var count = Deque<Int>()
    count.append(contentsOf: [0, 0, 0, 0, 0, 0, 0, 0, 0])
    
    // initial state
    for number in numbers {
        count[number] += 1
    }
    
    // simulation
    let days = 80
    for _ in 0 ..< days {
        let zeros = count.popFirst()!
        count.append(zeros)
        count[6] += zeros
    }
    
    print(count.reduce(0, +))
}

func day6_2() {
    let numbers = getInput()
    
    var count = Deque<Int>()
    count.append(contentsOf: [0, 0, 0, 0, 0, 0, 0, 0, 0])
    
    // initial state
    for number in numbers {
        count[number] += 1
    }
    
    // simulation
    let days = 256
    for _ in 0 ..< days {
        let zeros = count.popFirst()!
        count.append(zeros)
        count[6] += zeros
    }
    
    print(count.reduce(0, +))
}
