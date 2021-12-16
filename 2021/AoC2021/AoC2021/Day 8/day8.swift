import Foundation
import Collections

/*
 This day's code is a a bit of a mess. I tried to be too general for part 2 (classic), but my basic deductions
 weren't enough to get a unique mapping, so I ended up hacking an ugly second part on. It could be much tidier
 but I'm done with staring at it!
 */

private func getInput(file: String = "input.txt") -> [([String], [String])] {
    let url = Config.baseUrl.appendingPathComponent("Day 8/").appendingPathComponent(file)
    let strings = Utils.readLines(url: url)
    
//    let strings = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    
    let leftright = strings.map{$0.split(separator: "|")}
    let left = leftright.map {$0[0].split(separator: " ").filter {!$0.isEmpty}.map{String($0)}}
    let right = leftright.map {$0[1].split(separator: " ").filter {!$0.isEmpty}.map{String($0)}}
    return Array(zip(left, right))
}

func day8_1() {
    let patterns = getInput()
    
    // tempting to do this on one line with a chain of map/filter/reduce but think this is more readable!
    var count = 0
    for displayOutput in patterns.map({$0.1}) {
        for output in displayOutput {
            if output.count == 2 || output.count == 4 || output.count == 3 || output.count == 7 {
                // 1, 4, 7, 8
                count += 1
            }
        }
    }
    
    print(count)
}

class Mapping {
    static let canon = [0: "abcefg", 1: "cf", 2: "acdeg", 3: "acdfg", 4: "bcdf",
                        5: "abdfg", 6: "abdefg", 7: "acf", 8: "abcdefg", 9: "abcdfg"]
    
    static let canonSets = canon.mapValues({Set<Character>($0)})
    static let canonCounts = canon.mapValues({$0.count})
    
    var options = [Character: Set<Character>]()
    var finalMap = [Character: Character]()
    
    init() {
        for character in "abcdefg" {
            options[character] = Set("abcdefg")
        }
    }
    
    func processInputs(inputs: [String]) {
        var inputQueue = Deque(inputs.sorted(by: {$0.count < $1.count}))
        while !inputQueue.isEmpty && !options.mapValues({$0.count}).filter({$0.value > 1}).isEmpty {
            let input = Set(inputQueue.popFirst()!)
            
            let canonCharacters = Mapping.canonSets.filter {$0.value.count == input.count}.reduce(Set<Character>(), {$0.union($1.value)})
            
            for character in self.options.keys {
                if input.contains(character) {
                    self.options[character]?.formIntersection(canonCharacters)
                } else if input.count == canonCharacters.count {
                    self.options[character]?.subtract(canonCharacters)
                }
                
                if self.options[character]?.count == 0 {
                    fatalError()
                }
            }
            
            var singleValues = self.options.mapValues({$0.count}).filter({$0.value == 1})
            while !singleValues.isEmpty {
                for character in singleValues.keys {
                    self.finalMap[character] = self.options[character]!.first!
                    self.options.removeValue(forKey: character)
                    
                    let removeChar = String(self.finalMap[character]!)
                    for propagateCharacter in Set("abcdefg").subtracting(String(character)) {
                        self.options[propagateCharacter]?.subtract(removeChar)
                    }
                }
                singleValues = self.options.mapValues({$0.count}).filter({$0.value == 1})
            }
        }
        
        for value in [5, 6] {
            let inputsOfSizeN = inputs.filter {$0.count == value}
            let canonOfSizeN = Mapping.canon.values.filter {$0.count == value}
            
            for character in self.options.keys {
                let countInInput = inputsOfSizeN.filter {$0.contains(character)}.count
                let options = self.options[character]!
                for option in options {
                    let countInCanon = canonOfSizeN.filter {$0.contains(option)}.count
                    if countInInput != countInCanon {
                        self.options[character]!.remove(option)
                    }
                }
            }
            
            var singleValues = self.options.mapValues({$0.count}).filter({$0.value == 1})
            while !singleValues.isEmpty {
                for character in singleValues.keys {
                    self.finalMap[character] = self.options[character]!.first!
                    self.options.removeValue(forKey: character)
                    
                    let removeChar = String(self.finalMap[character]!)
                    for propagateCharacter in Set("abcdefg").subtracting(String(character)) {
                        self.options[propagateCharacter]?.subtract(removeChar)
                    }
                }
                singleValues = self.options.mapValues({$0.count}).filter({$0.value == 1})
            }
        }
    }
    
    func map(encodedWires: String) -> Int {
        if !options.mapValues({$0.count}).filter({$0.value > 1}).isEmpty {
            fatalError("non unique options")
        }
        
        let setWires = Set(encodedWires.map {self.finalMap[$0]!})
        
        return Mapping.canonSets.filter {$0.value == setWires}.first!.key
    }
}

func day8_2() {
    let patterns = getInput()
    
    var sum = 0
    
    for pattern in patterns {
        let mapping = Mapping()
        let inputs = pattern.0
        mapping.processInputs(inputs: inputs)
        
        let outputs = pattern.1
        let code = outputs.map {mapping.map(encodedWires: $0)}.reduce(0, {$0 * 10 + $1})
        
        print(code)
        
        sum += code
    }
    
    print()
    print(sum)
}
