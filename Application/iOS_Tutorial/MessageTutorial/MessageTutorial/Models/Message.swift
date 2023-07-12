//
//  Message.swift
//  MessageTutorial
//
//  Created by Nayeon Kim on 2023/07/12.
//

import Foundation

struct Message: Identifiable, Codable {
    var id: String
    var text: String
//    var received: Bool
    var user: String
    var timestamp: Date
}
