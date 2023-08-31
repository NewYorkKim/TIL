//
//  main.swift
//  Solve
//
//  Created by Nayeon Kim on 2023/08/31.
//

import Foundation

while true {
    let nums = readLine()!.split { $0 == " " }.map { Int($0)! }
    let a = nums[0], b = nums[1]
    
    if (a == 0) && (b == 0) {
        break
    } else {
        print(a + b)
    }
}
