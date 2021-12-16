import Foundation

private func getInput(file: String = "input.txt") -> [Int] {
    let url = Config.baseUrl.appendingPathComponent("Day 7/").appendingPathComponent(file)
    let strings = Utils.readLines(url: url)
    
    return strings[0].split(separator: ",").map {Int($0)!}
}

func fuelCost1(positions: [Int], moveTo: Int) -> Int {
    return positions.map {abs($0 - moveTo)}.reduce(0, +)
}

func nthTriangularNumber(n: Int) -> Int {
    return n*(n+1)/2
}

func fuelCost2(positions: [Int], moveTo: Int) -> Int {
    return positions.map {nthTriangularNumber(n: abs($0 - moveTo))}.reduce(0, +)
}

func day7_1() {
    let numbers = getInput()
    
    let median = numbers.sorted()[numbers.count / 2]
    
    let medianCost = fuelCost1(positions: numbers, moveTo: median)
    
    print(medianCost)
    
    // how did I know the median would be the right answer?
    // honestly, it was just a hunch, and I checked with brute force afterwards 😶
}

func day7_2() {
    let numbers = getInput()
    
    let mean = numbers.reduce(0, +) / numbers.count
    
    let cost1 = fuelCost2(positions: numbers, moveTo: mean-1)
    let cost2 = fuelCost2(positions: numbers, moveTo: mean)
    let cost3 = fuelCost2(positions: numbers, moveTo: mean+1)
    
    print(min(cost1, cost2, cost3))
    
    // this is one of the weirder AoC puzzles I remember doing (part 1 + 2)
    // super easy to brute force both parts, which I did use for my submission
    // reading the subreddit, there was some interesting theoretical analysis showing
    // the minimum for part two always lies within 0.5 of the mean, so the technique
    // above is sufficient
}
