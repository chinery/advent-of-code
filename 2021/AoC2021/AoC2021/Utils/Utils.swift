//
//  Utils.swift
//  AoC2021
//
//  Created by Andrew Chinery on 08/12/2021.
//

import Foundation

class Utils {
    static func readLines(url: URL) -> [String] {
        do {
            let data = try String(contentsOf: url)
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
