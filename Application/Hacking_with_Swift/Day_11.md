# 100 days of Swift

> 02.16.2023

- Day 11
- [source](https://www.hackingwithswift.com/100/1)

## 1. Protocols

- Protocols are a way of describing what properties and methods something must have

```swift
protocol Identifiable {
    var id: String { get set }
}

struct User: Identifiable {
    var id: String
}

func displayID(thing: Identifiable) {
    print("My ID is \(thing.id)")
}
```

## 2. Protocol Inheritance

```swift
protocol Payable {
    func calculateWages() -> Int
}

protocol NeedsTraining {
    func study()
}

protocol HasVacation {
    func takeVacatioin(days: Int)
}

protocol Employee: Payable, NeedsTrainig, HasVacation { }
```

## 3. Extensions

- Extensions allow you to add methods to existing types, to make them do things they weren't originally desinged to do

```swift
extension Int {
    func squared() -> Int {
        return self * self
    }
}

let number = 8
number.squared()

extension Int {
    var isEven: Bool {
        return self % 2 == 0
    }
}
```

## 4. Protocol Extensions

```swift
let pythons = ["Eric", "Graham", "John", "Michael", "Terry", "Terry"]
let beatles = Set(["John", "Paul", "George", "Ringo"])

extension Collection {
    func summarize() {
        print("There are \(count) of us:")

        for name in self {
            print(name)
        }
    }
}

pythons.summarize()
beatles.summarize()
```

## 5. Protocol-oriented Programming

- Crafting your code around protocols and protocol extensions

```swift
protocol Identifiable {
    var id: String { get set }
    func identify()
}

extension Identifiable {
    func identify() {
        print("My ID is \(id).")
    }
}

struct User: Identifiable {
    var id: String
}

let twostraws = User(id: "twostraws")
twotstraws.identify()
```