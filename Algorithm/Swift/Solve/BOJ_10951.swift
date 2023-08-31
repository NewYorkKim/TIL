//
//  main.swift
//  Solve
//
//  Created by Nayeon Kim on 2023/08/31.
//

import Foundation

while let nums = readLine() {
    let numsArr = nums.split { $0 == " " }.map { Int($0)! }
    let a = numsArr[0], b = numsArr[1]
    
    print(a + b)
}
