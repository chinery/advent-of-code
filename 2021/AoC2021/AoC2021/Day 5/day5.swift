import Foundation

private func extractInts(text: String) -> [Int] {
    let regex = try! NSRegularExpression(pattern: "[0-9]+")
    
    let results = regex.matches(in: text, range: NSRange(text.startIndex..., in: text))
    return results.map {
        Int(text[Range($0.range, in: text)!])!
    }
}

private func getInput(file: String = "input.txt") -> [Line] {
    let url = Config.baseUrl.appendingPathComponent("Day 5/").appendingPathComponent(file)
    let strings = Utils.readLines(url: url)
    
    return strings.map {
        let points = extractInts(text: $0)
        return Line(point1: Point(x: points[0], y: points[1]),
                    point2: Point(x: points[2], y: points[3]))
    }
}

struct Point: Hashable, Equatable {
    let x: Int, y: Int
}

struct Line {
    let point1: Point
    let point2: Point
    
    var isVertical: Bool { return self.point1.x == self.point2.x }
    var isHorizontal: Bool { return self.point1.y == self.point2.y }
    
    func rasterise() -> Set<Point> {
        if self.isVertical {
            let lower = point1.y < point2.y ? point1.y : point2.y
            let upper = point1.y < point2.y ? point2.y : point1.y
            
            return Set((lower...upper).map {Point(x: point1.x, y: $0)})
        } else if self.isHorizontal {
            let lower = point1.x < point2.x ? point1.x : point2.x
            let upper = point1.x < point2.x ? point2.x : point1.x
            
            return Set((lower...upper).map {Point(x: $0, y: point1.y)})
        } else {
            let lefter = point1.x < point2.x ? point1 : point2
            let righter = point1.x < point2.x ? point2 : point1
            
            let xRange = (lefter.x...righter.x)
            let yRange = lefter.y < righter.y ? Array(lefter.y...righter.y) : Array((righter.y...lefter.y).reversed())
            
            return Set(zip(xRange, yRange).map {Point(x: $0.0, y: $0.1)})
        }
    }
}

func day5_1() {
    var input = getInput()

    input = input.filter {$0.isVertical || $0.isHorizontal}
    
    var allPoints: Set<Point> = []
    var badPoints: Set<Point> = []
    
    for line in input {
        let linePoints = line.rasterise()
        badPoints.formUnion(allPoints.intersection(linePoints))
        allPoints.formUnion(linePoints)
    }
    
    print(badPoints.count)
}

func day5_2() {
    let input = getInput()
    
    var allPoints: Set<Point> = []
    var badPoints: Set<Point> = []
    
    for line in input {
        let linePoints = line.rasterise()
        badPoints.formUnion(allPoints.intersection(linePoints))
        allPoints.formUnion(linePoints)
    }
    
    print(badPoints.count)
}
