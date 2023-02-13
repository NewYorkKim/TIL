# 100 days of Swift

> 02.13.2023

- Day 8
- [source](https://www.hackingwithswift.com/100/1)

## 1. Creating Your Own Structs

- Swift lets you design your own types in two ways, of which the most common are called structures, or just *structs*
- Structs can be given their own variables and constants, and their own functions, then create and used however you want

```swift
struct Sport {
    var name: String
}

var tennis = Sport(name: "Tennis")
print(tennis.name)

tennis.name = "Lawn tennis"
```

## 2. Computed Properties

```swift
struct Sport {
    var name: String
    var isOlympicSport: Bool

    var olympicStatus: String {
        if isOlympicSport {
            return "\(name) is an Olympic sport"
        } else {
            return "\(name) is not an Olympic sport"
        }
    }
}
```

## 3. Property Observers

- Property observers let you run code before or after any property changes
- `didSet`: Take action *after* a property changes
- `willSet`: Take action *before* a property changes

```swift
struct Progress {
    var task: String
    var amount: Int
}

var progress = Progress(task: "Loading data", amout: 0)
progress.amount = 30
progress.amount = 80
progress.amount - 100

struct Progress {
    var task: String
    var amount: Int {
        didSet {
            prit("\(task) is now \(amount)% complete")
        }
    }
}
```

## 4. Methods

- Functions inside structs are called *methods*

```swift
struct City {
    var population: Int

    func collectTaxes() -> Int {
        return population * 1000
    }
}

let london = City(population: 9_000_000)
london.collectTaxes()
```

## 5. Mutating Methods

- Any time a struct's method tries to change any properties, you must mark it as `mutating`

```swift
struct Person {
    var name: String

    mutating func makeAnonymous() {
        name = "Anonymous"
    }
}

var person = Person(name: "Ed")
person.makeAnonymous()
```

## 6. Properties and Methods of Strings

```swift
let string = "Do or do not, there is no try."

print(string.count)
print(string.hasPrefix("Do"))
print(string.uppercased())
print(string.sorted())
```

## 7. Properties and Methods of Arrays

```swift
var toys = ["Woody"]

print(toys.count)
toys.append("Buzz")
toys.firstIndex(of: "Buzz")
print(toys.sorted())
toys.remove(at: 0)
```