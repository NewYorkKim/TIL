//
//  main.swift
//  Solve
//
//  Created by Nayeon Kim on 2023/09/01.
//

import Foundation

let n = Double(readLine()!)!
var scores = readLine()!.split { $0 == " " }.map { Double($0)! }
let maxScore = scores.max()!

scores = scores.map { $0 / maxScore * 100 }

let result = scores.reduce(0.0, +) / n

print(result)
