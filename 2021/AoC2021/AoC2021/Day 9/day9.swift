import Foundation
import DequeModule

private func getInput(file: String = "input.txt") -> [[Int]] {
    let url = Config.baseUrl.appendingPathComponent("Day 9/").appendingPathComponent(file)
    let strings = Utils.readLines(url: url)

//    let strings = """
//    2199943210
//    3987894921
//    9856789892
//    8767896789
//    9899965678
//    """.split(separator: "\n")
    
    return strings.map{$0.map{Int(String($0))!}}
}

func day9_1() {
    let heightMap = getInput()
    
    var sum = 0
    
    for i in 0 ..< heightMap.count {
        for j in 0 ..< heightMap[i].count {
            let point = heightMap[i][j]
            if (i > 0 && heightMap[i-1][j] <= point) ||
               (i < heightMap.count - 1 && heightMap[i+1][j] <= point) ||
               (j > 0 && heightMap[i][j-1] <= point) ||
               (j < heightMap[i].count - 1 && heightMap[i][j+1] <= point) {
                continue
            }
            sum += point + 1
        }
    }
    
    print(sum)
}

func day9_2() {
    let heightMap = getInput()
    
    var basinTerminals = Set<Point>()
    
    for i in 0 ..< heightMap.count {
        for j in 0 ..< heightMap[i].count {
            let point = heightMap[i][j]
            if (i > 0 && heightMap[i-1][j] <= point) ||
               (i < heightMap.count - 1 && heightMap[i+1][j] <= point) ||
               (j > 0 && heightMap[i][j-1] <= point) ||
               (j < heightMap[i].count - 1 && heightMap[i][j+1] <= point) {
                continue
            }
            
            basinTerminals.insert(Point(x: j, y: i))
        }
    }
    
    var basins = [Set<Point>]()
    while !basinTerminals.isEmpty {
        var thisBasin = Set<Point>()
        var frontier = Deque<Point>()

        let point = basinTerminals.removeFirst()
        thisBasin.insert(point)
        frontier.append(point)
        
        while !frontier.isEmpty {
            let explore = frontier.popFirst()!
            
            for candidate in [Point(x: explore.x + 1, y: explore.y),
                              Point(x: explore.x - 1, y: explore.y),
                              Point(x: explore.x, y: explore.y + 1),
                              Point(x: explore.x, y: explore.y - 1)] {
                
                if !frontier.contains(candidate) && !thisBasin.contains(candidate)
                    && candidate.x >= 0 && candidate.x < heightMap[0].count
                    && candidate.y >= 0 && candidate.y < heightMap.count
                    && heightMap[candidate.y][candidate.x] < 9
                {
                    thisBasin.insert(candidate)
                    frontier.append(candidate)
                }
            }
        }
        
        basins.append(thisBasin)
    }
    
    print(basins.map({$0.count}).sorted().reversed()[0...2].reduce(1, *))
}
