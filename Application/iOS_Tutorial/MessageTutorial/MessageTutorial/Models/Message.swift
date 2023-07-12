//
//  Message.swift
//  MessageTutorial
//
//  Created by Nayeon Kim on 2023/07/12.
//

import Foundation

struct Message: Identifiable, Codable {
    var id: UUID
    var text: String
    var received: Bool
    var timestamp: Date
}
