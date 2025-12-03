import Foundation
import Collections

private func getInput(file: String = "input.txt") -> [[Int]] {
    let url = Config.baseUrl.appendingPathComponent("Day 11/").appendingPathComponent(file)
    let strings = Utils.readLines(url: url)
    
//    let strings = """
//        5483143223
//        2745854711
//        5264556173
//        6141336146
//        6357385478
//        4167524645
//        2176841721
//        6882881134
//        4846848554
//        5283751526
//        """.split(separator: "\n")
    
    return strings.map{$0.map{Int(String($0))!}}
}

func day11_1() {
    let octoEnergy = getInput()
    var octoEnergyFlashed = octoEnergy.map {$0.map{(energy: $0, flashed: false)}}
    
    var totalFlashed = 0
    
    for _ in 0 ..< 100 {
        var toFlash = Deque<Point>()
        
        for i in 0 ..< octoEnergyFlashed.count {
            for j in 0 ..< octoEnergyFlashed[0].count {
                octoEnergyFlashed[i][j].energy += 1
                octoEnergyFlashed[i][j].flashed = false
                
                if octoEnergyFlashed[i][j].energy > 9 {
                    toFlash.append(Point(x: j, y: i))
                }
            }
        }
        
        while !toFlash.isEmpty {
            let flasher = toFlash.popFirst()!
            octoEnergyFlashed[flasher.y][flasher.x].flashed = true
            octoEnergyFlashed[flasher.y][flasher.x].energy = 0
            
            totalFlashed += 1
            
            for di in -1 ... 1 {
                for dj in -1 ... 1 {
                    let i = flasher.y + di
                    let j = flasher.x + dj
                    
                    if i >= 0 && i < octoEnergyFlashed.count
                        && j >= 0 && j < octoEnergyFlashed[i].count
                        && !octoEnergyFlashed[i][j].flashed {
                        octoEnergyFlashed[i][j].energy += 1
                        
                        if octoEnergyFlashed[i][j].energy > 9 {
                            let pt = Point(x: j, y: i)
                            if !toFlash.contains(pt) {
                                toFlash.append(Point(x: j, y: i))
                            }
                        }
                    }
                }
            }
        }
    }
    
    print(totalFlashed)
}

func day11_2() {
    let octoEnergy = getInput()
    var octoEnergyFlashed = octoEnergy.map {$0.map{(energy: $0, flashed: false)}}
    
    for step in 0 ..< 1000 {
        var toFlash = Deque<Point>()
        
        for i in 0 ..< octoEnergyFlashed.count {
            for j in 0 ..< octoEnergyFlashed[0].count {
                octoEnergyFlashed[i][j].energy += 1
                octoEnergyFlashed[i][j].flashed = false
                
                if octoEnergyFlashed[i][j].energy > 9 {
                    toFlash.append(Point(x: j, y: i))
                }
            }
        }
        
        while !toFlash.isEmpty {
            let flasher = toFlash.popFirst()!
            octoEnergyFlashed[flasher.y][flasher.x].flashed = true
            octoEnergyFlashed[flasher.y][flasher.x].energy = 0
            
            for di in -1 ... 1 {
                for dj in -1 ... 1 {
                    let i = flasher.y + di
                    let j = flasher.x + dj
                    
                    if i >= 0 && i < octoEnergyFlashed.count
                        && j >= 0 && j < octoEnergyFlashed[i].count
                        && !octoEnergyFlashed[i][j].flashed {
                        octoEnergyFlashed[i][j].energy += 1
                        
                        if octoEnergyFlashed[i][j].energy > 9 {
                            let pt = Point(x: j, y: i)
                            if !toFlash.contains(pt) {
                                toFlash.append(Point(x: j, y: i))
                            }
                        }
                    }
                }
            }
        }
        
        if octoEnergyFlashed.joined().filter({!$0.flashed}).isEmpty {
            print("Synchronised flash after step", step + 1)
            return
        }
    }
}
