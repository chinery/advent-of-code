import Foundation
import simd

private func getInput(file: String) -> [simd_int2] {
    let baseUrl = URL(fileURLWithPath: "/Users/andrew/dev/advent-of-code/2021/AoC2021/AoC2021/Day 2/")
    let url = baseUrl.appendingPathComponent(file)
    let strings = Utils.readLines(url: url)
    
    return strings.map {$0.split(separator: " ")}
    .map {
        if $0[0] == "forward" {
            return simd_int2(Int32($0[1])!, 0)
        } else if $0[0] == "up" {
            return simd_int2(0, -Int32($0[1])!)
        } else {
            return simd_int2(0, Int32($0[1])!)
        }
    }
}

func day2_1() {
    let input = getInput(file: "input.txt")
    
    let position = input.reduce(simd_int2(0, 0)) { result, next in
        return result &+ next
    }
    
    print(position.x * position.y)
}


func day2_2() {
    let input = getInput(file: "input.txt")
    
    let position = input.reduce(simd_int3(0, 0, 0)) { result, next in
        if next.x == 0 {
            return result &+ simd_int3(0, 0, next.y)
        } else {
            return result &+ simd_int3(next.x, result.z * next.x, 0)
        }
    }
    
    print(position.x * position.y)
}
