//
//  Task.swift
//  RealmTutorial
//
//  Created by Nayeon Kim on 2023/05/02.
//

import Foundation
import RealmSwift

class Task: Object, ObjectKeyIdentifiable {
    @Persisted(primaryKey: true) var id: ObjectId
    @Persisted var title = ""
    @Persisted var completed = false
}
