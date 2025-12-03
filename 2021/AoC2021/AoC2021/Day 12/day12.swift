import Foundation
import Collections

private func getInput(file: String = "input.txt") -> [(cave1: String, cave2: String)] {
    let url = Config.baseUrl.appendingPathComponent("Day 12/").appendingPathComponent(file)
    let strings = Utils.readLines(url: url)
    
//    let strings = """
//        start-A
//        start-b
//        A-c
//        A-b
//        b-d
//        A-end
//        b-end
//        """.split(separator: "\n")
    
    return strings.map{
        let split = $0.split(separator: "-")
        return (String(split[0]), String(split[1]))
    }
}

func day12_1() {
    let inputRules = getInput()
    let rules: [(from: String, to: String)] = inputRules.map {(from: $0.cave1, to: $0.cave2)}
                                              + inputRules.map {(from: $0.cave2, to: $0.cave1)}
    
    var frontier = Deque<[String]>()
    frontier.append(["start"])
    
    var paths = [[String]]()
    
    while !frontier.isEmpty {
        let explorePath = frontier.popFirst()!
        
        for rule in rules.filter({$0.from == explorePath.last!}) {
            if rule.to.uppercased() != rule.to && explorePath.contains(rule.to) {
                continue
            }
            
            let path = explorePath + [rule.to]
            
            if rule.to == "end" {
                paths.append(path)
            } else {
                frontier.append(path)
            }
        }
    }
    
    print(paths.count)
}

func day12_2() {
    let inputRules = getInput()
    let rules: [(from: String, to: String)] = (inputRules.map {(from: $0.cave1, to: $0.cave2)}
                                               + inputRules.map {(from: $0.cave2, to: $0.cave1)})
            .filter {$0.to != "start" && $0.from != "end"}
    
    
    
    var frontier = Deque<(path: [String], doubleVisitedSmall: Bool)>()
    frontier.append((["start"], false))
    
    var paths = [[String]]()
    
    while !frontier.isEmpty {
        let explorePath = frontier.popFirst()!
        
        for rule in rules.filter({$0.from == explorePath.path.last!}) {
            var doubleVisitedSmall = explorePath.doubleVisitedSmall
            
            if rule.to.uppercased() != rule.to && explorePath.path.contains(rule.to) {
                if explorePath.doubleVisitedSmall {
                    continue
                } else {
                    doubleVisitedSmall = true
                }
            }
            
            let path = explorePath.path + [rule.to]
            
            if rule.to == "end" {
                paths.append(path)
            } else {
                frontier.append((path, doubleVisitedSmall))
            }
        }
    }
    
    print(paths.count)
}
