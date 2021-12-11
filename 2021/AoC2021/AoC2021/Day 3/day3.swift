import Foundation

private func getInput(file: String = "input.txt") -> [String] {
    let url = Config.baseUrl.appendingPathComponent("Day 3/").appendingPathComponent(file)
    let strings = Utils.readLines(url: url)
    
    return strings
}

func day3_1() {
    let input = getInput()
    
    var counts = Array(repeating: 0, count: input.first!.count)
    
    for binary in input {
        for (i, digit) in binary.enumerated() {
            if digit == "1" {
                counts[i] += 1
            }
        }
    }
    
    var gamma = 0.0
    var epsilon = 0.0
    
    for (i, count) in counts.reversed().enumerated() {
        if count > input.count / 2 {
            gamma += pow(2, Double(i))
        } else {
            epsilon += pow(2, Double(i))
        }
    }
    
    print(Int(gamma * epsilon))
}

func mostCommonBinaryDigit(numbers: [String], column: Int) -> String.Element {
    var count = 0.0
    for binary in numbers {
        if binary[binary.index(binary.startIndex, offsetBy: column)] == "1" {
            count += 1
        }
    }
    
    return count >= (Double(numbers.count) / 2.0) ? "1" : "0"
}

func leastCommonBinaryDigit(numbers: [String], column: Int) -> String.Element {
    var count = 0.0
    for binary in numbers {
        if binary[binary.index(binary.startIndex, offsetBy: column)] == "1" {
            count += 1
        }
    }
    
    return count < Double(numbers.count) / 2.0 ? "1" : "0"
}

func day3_2() {
    let originalInput = getInput()
    var input = originalInput
    
    var i = 0
    while input.count > 1 {
        let common = mostCommonBinaryDigit(numbers: input, column: i)
        
        input = input.filter {$0[$0.index($0.startIndex, offsetBy: i)] == common}
        i += 1
    }
    let oxygen = input.first!
    
    input = originalInput
    i = 0
    while input.count > 1 {
        let common = leastCommonBinaryDigit(numbers: input, column: i)
        
        input = input.filter {$0[$0.index($0.startIndex, offsetBy: i)] == common}
        i += 1
    }
    let co2 = input.first!
    
    print(Int(oxygen, radix: 2)! * Int(co2, radix: 2)!)
}
