import Collections
import Foundation

struct Utils {
    static func readLines(filename: String) -> [String] {
        do {
            let data = try String(contentsOfFile: filename)
            let lines = data.components(separatedBy: .newlines)

            if let last = lines.last, last == "" {
                return Array(lines.prefix(upTo: lines.count - 1))
            } else {
                return lines
            }
        } catch {
            print(error)
            fatalError()
        }
    }
}

struct ButtonWiring: CustomDebugStringConvertible {
    let positionsAffected: [Int]

    init(from input: String) {
        // (0,1,2,3,4)
        let start = input.index(input.startIndex, offsetBy: 1)
        let end = input.index(input.endIndex, offsetBy: -1)
        self.positionsAffected = input[start..<end].split(separator: ",").map({ Int($0)! })
    }

    var debugDescription: String {
        return "(\(self.positionsAffected.map({String($0)}).joined(separator: ",")))"
    }
}

struct Joltages: CustomDebugStringConvertible {
    var values: [Int]

    init(from input: String) {
        // e.g. {3,5,4,7}
        let start = input.index(input.startIndex, offsetBy: 1)
        let end = input.index(input.endIndex, offsetBy: -1)
        self.values = input[start..<end].split(separator: ",").map({ Int($0)! })
    }

    init(length: Int) {
        self.values = Array(repeating: 0, count: length)
    }

    func subarray(indices: [Int]) -> Joltages {
        var newJolts = Joltages(length: indices.count)
        for (thisI, newI) in indices.enumerated() {
            newJolts.values[newI] = self.values[thisI]
        }
        return newJolts
    }

    static func == (lhs: Joltages, rhs: Joltages) -> Bool {
        for (lhsJoltage, rhsJoltage) in zip(lhs.values, rhs.values) {
            if lhsJoltage != rhsJoltage {
                return false
            }
        }
        return true
    }

    func applyButtonWiring(buttonWiring: ButtonWiring) -> Joltages {
        var newLights = self
        for lightToggled in buttonWiring.positionsAffected {
            newLights.values[lightToggled] += 1
        }
        return newLights
    }

    var count: Int {
        return self.values.count
    }

    var debugDescription: String {
        return "{\(self.values.map({String($0)}).joined(separator: ","))}"
    }
}

struct Lights: CustomDebugStringConvertible {
    var lights: [Bool]

    static let EMPTY: Lights = Lights(length: 0)

    init(from input: String) {
        // e.g. [.###.#]
        let start = input.index(input.startIndex, offsetBy: 1)
        let end = input.index(input.endIndex, offsetBy: -1)
        self.lights = input[start..<end].map({ $0 == "#" })
    }

    init(length: Int) {
        self.lights = Array(repeating: false, count: length)
    }

    static func == (lhs: Lights, rhs: Lights) -> Bool {
        for (lhsLight, rhsLight) in zip(lhs.lights, rhs.lights) {
            if lhsLight != rhsLight {
                return false
            }
        }
        return true
    }

    func applyButtonWiring(buttonWiring: ButtonWiring) -> Lights {
        var newLights = self
        for lightToggled in buttonWiring.positionsAffected {
            newLights.lights[lightToggled] = !newLights.lights[lightToggled]
        }
        return newLights
    }

    var count: Int {
        return self.lights.count
    }

    var debugDescription: String {
        return "[\(self.lights.map({$0 ? "#" : "."}).joined(separator: ""))]"
    }
}

struct FactoryMachine {
    let lightsTarget: Lights
    let joltagesTarget: Joltages
    let buttonWirings: [ButtonWiring]
}
extension FactoryMachine {
    init(from input: String) {
        let parts = input.split(separator: " ")
        guard let targetPart = parts.first else { fatalError() }
        guard let joltagePart = parts.last else { fatalError() }

        self.lightsTarget = Lights(from: String(targetPart))

        self.joltagesTarget = Joltages(from: String(joltagePart))

        self.buttonWirings = parts[1..<parts.count - 1].map({ ButtonWiring(from: String($0)) })
    }
}

struct LightSearchState: Comparable {
    let lights: Lights
    let cost: Int

    static func < (lhs: LightSearchState, rhs: LightSearchState) -> Bool {
        return lhs.cost < rhs.cost
    }

    static func == (lhs: LightSearchState, rhs: LightSearchState) -> Bool {
        return lhs.cost == rhs.cost
    }

    init(_ lights: Lights, _ cost: Int) {
        self.lights = lights
        self.cost = cost
    }
}

private func solvePart1(machine: FactoryMachine) -> Int {
    let lights = Lights(length: machine.lightsTarget.count)
    var frontier: Heap<LightSearchState> = [LightSearchState(lights, 0)]

    while !frontier.isEmpty {
        guard let bestSoFar = frontier.popMin() else { fatalError() }

        for buttonWiring in machine.buttonWirings {
            let newLights = bestSoFar.lights.applyButtonWiring(buttonWiring: buttonWiring)
            let cost = bestSoFar.cost + 1

            if newLights == machine.lightsTarget {
                return cost
            }

            frontier.insert(LightSearchState(newLights, cost))
        }
    }

    fatalError("Exhausted search space")
}

private func day10part1(machines: [FactoryMachine]) {
    print(machines.reduce(0, { acc, machine in acc + solvePart1(machine: machine) }))
}

// generates all arrays of length n of ints >= 0 that sum to sum
private func generateButtonPresses(n: Int, sum: Int) -> [[Int]] {
    if n == 1 {
        return [[sum]]
    }
    if sum == 0 {
        return [Array(repeating: 0, count: n)]
    }

    var allPresses: [[Int]] = []
    for x in (0...sum).reversed() {
        let subpresses = generateButtonPresses(n: n - 1, sum: sum - x)
        for subpress in subpresses {
            allPresses.append([x] + subpress)
        }
    }
    return allPresses
}

struct Constraint: Equatable, Hashable {
    let buttonIndices: Set<Int>
    let sumTo: Int

    func reduction(otherConstraint: Constraint) -> Constraint {
        return Constraint(
            buttonIndices: self.buttonIndices.subtracting(otherConstraint.buttonIndices),
            sumTo: self.sumTo - otherConstraint.sumTo
        )
    }
}

extension Set<Constraint> {
    func clashes(_ constraint: Constraint) -> Bool {
        return self.contains(where: {
            $0.buttonIndices == constraint.buttonIndices && $0.sumTo != constraint.sumTo
        })
    }

    func reduceRow(constraint: Constraint) -> Set<Constraint> {
        var newConstraints = Set<Constraint>()
        for otherConstraint in self {
            if constraint.buttonIndices.isSuperset(of: otherConstraint.buttonIndices) {
                let reduction = constraint.reduction(otherConstraint: otherConstraint)
                newConstraints.insert(reduction)
            }
        }
        return newConstraints
    }
}

class ConstraintSystem {
    var constraints: Set<Constraint>
    var invalid = false

    init(constraints: Set<Constraint>) {
        self.constraints = constraints
    }

    private func reduceSet() -> Bool {
        var newConstraints = Set<Constraint>()
        for constraint in self.constraints {
            let reduced = self.constraints.subtracting(Set<Constraint>([constraint])).reduceRow(
                constraint: constraint)

            if reduced.contains(where: {self.constraints.clashes($0) || $0.sumTo < 0}) {
                self.invalid = true
                return false
            }

            if reduced.isEmpty {
                newConstraints.insert(constraint)
            } else {
                newConstraints.formUnion(reduced)
            }
        }
        if newConstraints != self.constraints {
            self.constraints = newConstraints
            return true
        }
        return false
    }

    func reduceAll() {
        while self.reduceSet() {}
    }

    var unsolvedConstraints: [Constraint] {
        self.constraints.filter({ $0.buttonIndices.count > 1 })
    }

    func printSystem() {
        let sortedConstraints = self.constraints.sorted(by: { $0.sumTo < $1.sumTo }).sorted(by: {
            $0.buttonIndices.count < $1.buttonIndices.count
        })
        for constraint in sortedConstraints {
            print("\(constraint.buttonIndices.sorted()) = \(constraint.sumTo)")
        }
    }

    func printMatrix() {
        let maxButton = self.constraints.map({ $0.buttonIndices.max()! }).max()!
        let sortedConstraints = self.constraints.sorted(by: { $0.sumTo < $1.sumTo }).sorted(by: {
            $0.buttonIndices.count < $1.buttonIndices.count
        })
        for constraint in sortedConstraints {
            for i in 0...maxButton {
                if constraint.buttonIndices.contains(i) {
                    print("1", terminator: "")
                } else {
                    print(".", terminator: "")
                }
            }
            print(" | \(constraint.sumTo)")
        }
    }
}

private func solveSystem(_ cs: ConstraintSystem) -> Int {
    cs.reduceAll()

    if cs.invalid {
        return -1
    }

    if cs.unsolvedConstraints.count == 0 {
        return cs.constraints.reduce(0, { (acc, elm) in acc + elm.sumTo })
    }

    let constraint = cs.unsolvedConstraints.sorted(by: {
        $0.buttonIndices.count < $1.buttonIndices.count
    }).sorted(by: { $0.sumTo < $1.sumTo }).first!
    
    let buttonIndices = constraint.buttonIndices.sorted()
    let options = generateButtonPresses(n: buttonIndices.count, sum: constraint.sumTo)
    
    var bestCost = -1
    for option in options {
        var constraints = cs.constraints
        for (index, value) in zip(buttonIndices, option) {
            constraints.insert(Constraint(buttonIndices: [index], sumTo: value))
        }
        let newCS = ConstraintSystem(constraints: constraints)
        let cost = solveSystem(newCS)
        if cost > 0 && (bestCost == -1 || cost < bestCost) {
            bestCost = cost
        }
    }
    return bestCost
}


private func solvePart2(machine: FactoryMachine) -> Int {
    var buttonAffectsDict: [Int: [Int]] = Dictionary()
    for (buttonIndex, button) in machine.buttonWirings.enumerated() {
        for index in button.positionsAffected {
            if buttonAffectsDict[index] == nil {
                buttonAffectsDict[index] = []
            }
            buttonAffectsDict[index]!.append(buttonIndex)
        }
    }

    var constraints: Set<Constraint> = []
    for (key:joltageIndex, value:buttons) in buttonAffectsDict {
        let constraint = Constraint(
            buttonIndices: Set(buttons), sumTo: machine.joltagesTarget.values[joltageIndex])

        constraints.insert(constraint)
    }

    let system = ConstraintSystem(constraints: constraints)
    return solveSystem(system)
}

private func day10part2(machines: [FactoryMachine]) {
    var total = 0
    for machine in machines {
        let machineCost = solvePart2(machine: machine)
        print("...\(machineCost)")
        total += machineCost
    }
    print(total)
}

@main
struct _0 {
    static func main() {
        let filename = "10.txt"
        let data = Utils.readLines(filename: filename)
        let machines = data.map({ FactoryMachine(from: $0) })

        // day10part1(machines: machines)
        day10part2(machines: machines)
    }
}
