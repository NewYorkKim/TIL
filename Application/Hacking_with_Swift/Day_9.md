# 100 days of Swift

> 02.14.2023

- Day 9
- [source](https://www.hackingwithswift.com/100/1)

## 1. Initializers

- Special methods taht provide different ways to create your struct
- All structs come with one by default, called their *memberwise initializer* – this asks you to provide a value for each property when you create the struct

```swift
struct User {
    var username: String
}

var user = User(username: "twostraws")

struct User {
    var username: String

    init() {
        username = "Anonymous"
        print("Creating a new user!")
    }
}

var user = User()
user.username = "twostraws"
```

## 2. Referring to the Current Instance

- Inside methods you get a special constant called `self`, which points to whatever instance of the struct is currently being used
- This `self` value is particularly useful when you create initalizers that have the same parameter names as your property

```swift
struct Person {
    var name: String

    init(name: String) {
        print("\(name) was born!")
        self.name = name
    }
}
```

## 3. Lazy Properties

```swift
struct FamilyTree {
    init() {
        print("Creating family tree!")
    }
}

struct Person {
    var name: String
    lazy var familyTree = FamilyTree()

    init(name: String) {
        self.name = name
    }
}

var ed = Person(name: "Ed")

ed.familyTree
```

## 4. Static Properties and Methods

```swift
struct Student {
    var name: String

    init(name: String) {
        self.name = name
    }
}

let ed Student(name: "Ed")
let taylor = Student(name: "Taylor")

struct Student {
    static var classSize = 0
    var name: String

    init(name: String) {
        self.name = name
        Student.classSize += 1
    }
}

print(Student.classSize)
```

## 5. Access Control

- Access control lets you restrict which code can use properties and methods

```swift
struct Person {
    var.id: String

    init(id: String) {
        self.id = id
    }
}

let ed = Person(id: "12345")

struct Person {
    private var id: String

    init(id: String) {
        self.id = id
    }

    func identify() -> String {
        return "My social security number is \(id)"
    }
}
```