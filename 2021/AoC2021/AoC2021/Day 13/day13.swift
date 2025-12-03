import Foundation

private func getInput(file: String = "input.txt") -> String {
    let mapping: [Character: String] =
        ["0": "0000",
         "1": "0001",
         "2": "0010",
         "3": "0011",
         "4": "0100",
         "5": "0101",
         "6": "0110",
         "7": "0111",
         "8": "1000",
         "9": "1001",
         "A": "1010",
         "B": "1011",
         "C": "1100",
         "D": "1101",
         "E": "1110",
         "F": "1111"]
    
    
    let url = Config.baseUrl.appendingPathComponent("Day 13/").appendingPathComponent(file)
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
    
    return strings[0].map {mapping[$0]!}.joined()
}
