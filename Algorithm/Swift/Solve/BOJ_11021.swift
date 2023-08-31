//
//  main.swift
//  Solve
//
//  Created by Nayeon Kim on 2023/08/31.
//

import Foundation

let t = Int(readLine()!)!

for i in 1...t {
    let nums = readLine()!.split{ $0 == " " }.map { Int($0)! }
    let a = nums[0], b = nums[1]
    let result = a + b
    
    print("Case #\(i): \(result)")
}
