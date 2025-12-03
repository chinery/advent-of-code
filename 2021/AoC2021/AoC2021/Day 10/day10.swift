import Foundation
import Collections

private func getInput(file: String = "input.txt") -> [String] {
    let url = Config.baseUrl.appendingPathComponent("Day 10/").appendingPathComponent(file)
    let strings = Utils.readLines(url: url)
    
//    let strings = """
//[({(<(())[]>[[{[]{<()<>>
//[(()[<>])]({[<{<<[]>>(
//{([(<{}[<>[]}>{[]{[(<()>
//(((({<>}<{<{<>}{[]{[]{}
//[[<[([]))<([[{}[[()]]]
//[{[{({}]{}}([{[{{{}}([]
//{<[[]]>}<{[{[{[]{()[[[]
//[<(<(<(<{}))><([]([]()
//<{([([[(<>()){}]>(<<{{
//<{([{{}}[<[[[<>{}]]]>[]]
//""".split(separator: "\n").map({String($0)})
    
    return strings
}

enum ChunkChar {
    case paren, square, curly, angled
}

func day10_1() {
    let lines = getInput()
    
    var cost = 0
    for line in lines {
        var stack = Deque<ChunkChar>()
        var end = false
        
        for chr in line {
            switch chr {
            case "(": stack.append(.paren)
            case "[": stack.append(.square)
            case "{": stack.append(.curly)
            case "<": stack.append(.angled)
            case ")":
                if stack.popLast() != .paren {
                    cost += 3
                    end = true
                }
            case "]":
                if stack.popLast() != .square {
                    cost += 57
                    end = true
                }
            case "}":
                if stack.popLast() != .curly {
                    cost += 1197
                    end = true
                }
            case ">":
                if stack.popLast() != .angled {
                    cost += 25137
                    end = true
                }
            default: break
            }
            
            if end {
                break
            }
        }
    }
    
    print(cost)
}


func day10_2() {
    let lines = getInput()
    
    var scores = [Int]()
    
    for line in lines {
        var stack = Deque<ChunkChar>()
        var end = false
        
        for chr in line {
            switch chr {
            case "(": stack.append(.paren)
            case "[": stack.append(.square)
            case "{": stack.append(.curly)
            case "<": stack.append(.angled)
            case ")":
                if stack.popLast() != .paren {
                    end = true
                }
            case "]":
                if stack.popLast() != .square {
                    end = true
                }
            case "}":
                if stack.popLast() != .curly {
                    end = true
                }
            case ">":
                if stack.popLast() != .angled {
                    end = true
                }
            default: break
            }
            
            if end {
                break
            }
        }
        if end {
            continue
        }
        
        // incomplete line
        var score = 0
        while !stack.isEmpty {
            let char = stack.popLast()!
            score *= 5
            switch char {
            case .paren:
                score += 1
            case .square:
                score += 2
            case .curly:
                score += 3
            case .angled:
                score += 4
            }
        }
        
        scores.append(score)
    }
    
    print(scores.sorted()[scores.count / 2])
}
