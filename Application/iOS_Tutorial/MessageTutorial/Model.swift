//
//  Model.swift
//  MessageTutorial
//
//  Created by Nayeon Kim on 2023/07/11.
//

struct Message {
    var content: String
    var user: User
}

struct User {
    var name: String
    var profileImg: String = "person.circle.fill"
    var isCurrentUser: Bool = false
}
