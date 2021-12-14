import Foundation

private func getInput(file: String = "input.txt") -> ([BingoCard], [Int]) {
    let url = Config.baseUrl.appendingPathComponent("Day 4/").appendingPathComponent(file)
    let strings = Utils.readLines(url: url)
    
    let numbers = strings[0].split(separator: ",").map {Int($0)!}
    
    var cards = [BingoCard]()
    var card = BingoCard()
    
    for line in strings[2...] {
        if line != "" {
            card.addRow(numbers: line.split(separator: " ").map({Int($0)!}))
        } else {
            cards.append(card)
            card = BingoCard()
        }
    }
    
    return (cards, numbers)
}

class BingoCard {
    var numbers: [[(number: Int, marked: Bool)]] = [[(Int, Bool)]]()
    var won: Bool = false
    
    func addRow(numbers: [Int]) {
        self.numbers.append(numbers.map {(number: $0, marked: false)})
    }
    
    func markNumber(number: Int) -> Bool {
        for i in 0 ..< self.numbers.count {
            for j in 0 ..< self.numbers[i].count {
                if self.numbers[i][j].number == number {
                    self.numbers[i][j].marked = true
                    
                    if self.numbers[i].filter({$0.marked == false}).isEmpty {
                        self.won = true
                        return true
                    } else if self.numbers.map({$0[j]}).filter({$0.marked == false}).isEmpty {
                        self.won = true
                        return true
                    } else {
                        return false
                    }
                }
            }
        }
        return false
    }
    
    func sumOfUnmarked() -> Int {
        return self.numbers.map {
            $0.filter {$0.marked == false}
            .map {$0.number}
            .reduce(0, +)
        }.reduce(0, +)
    }
}

func day4_1() {
    let (cards, numbers) = getInput()
    
    for number in numbers {
        for card in cards {
            if card.markNumber(number: number) {
                print(number * card.sumOfUnmarked())
                return
            }
        }
    }
}

func day4_2() {
    let (cards, numbers) = getInput()
    
    for number in numbers {
        for card in cards {
            if card.won == false && card.markNumber(number: number) {
                print(number * card.sumOfUnmarked())
            }
        }
    }
}
