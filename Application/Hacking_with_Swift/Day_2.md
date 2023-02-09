# 100 days of Swift

> 02.09.2023

- Day 2
- [source](https://www.hackingwithswift.com/100/1)

## 1. Arrays

- Collections of values that are stored as a single value
- Using type annotations, arrays are written in brackets: [String], [Int], [Double], and [Bool]
- Counting from 0

```swift
let john = "John Lennon"
let paul = "Paul McCartney"
let george = "George Harrison"
let ringo = "Ringo Starr"

let beatles = [john, paul, george, ringo]

beatles[1]
```

## 2. Sets

- Collections of values just like arrays, except they have two differences
    1. Items aren't stored in any order
    2. No item can appear twice in a set
- Sets are more useful than arrays for times when you want to say "does this item exist?"

```swift
let colors = Set(["red", "green", "blue"])
let colors2 = Set(["red", "green", "blue", "red", "blue"])
```

## 3. Tuples

- You can't add or remove items from a tuple
- You can't change the type of items in a tuple
- You can access items in a tuple using numerical positions or by naming them

```swift
var name = (first: "Taylor", last: "Swift")

name.0
name.first
```

## 4. Arrays vs. Sets vs. Tuples

- They have distinct uses
- Arrays
    - A collection of values that can contain duplicates
    - the order of your items matters
- Sets
    - A collection of values that must be unique
    - To check whether a specific item is in there extremely quickly
- Tuples
    - A specific, fixed collection of related values where each item has a precise position or name

```swift
let address = (house: 555, street: "Taylor Swift Avenue", city: "Nashville")
let set = Set(["aardvark", "astronaut", "azalea"])
let pythons = ["Eric", "Graham", "John", "Michael", "Terry", "Terry"]
```

## 5. Dictionaries

- Collections of values just like arrays, but rather than storing things with an integer position you can access them using anythin you want
- Using type annotations, dictionaries are written in brackets with a colon between your identifier and value types
    - [String: Double],  [String: String]

```swift
let height = [
    "Taylor Swift": 1.78,
    "Ed Sheeran": 1.73
]

heights["Taylor Swift"]
```

## 6. Dictionary Default Values

- If you try to read a value from a dictionary using a key that doesn't exist, Swift will send you back `nil` – nothing at all
- We can provide the dictionary with a default value to use if we request a missing key

```swift
let favoriteIceCream = [
    "Paul": "Chocolate",
    "Sophie": "Vanilla" 
]

favoriteIceCream["Charlotte"]

favoriteIceCream["Charlotte", default: "Unkown"]
```

## 7. Creating Empty Collections

```swift
var teams = [String: String]()
var results = [Int]()

teams["Paul"] = "Red"

var words = Set<String>()
var numbers = Set<Int>()
var scores = Dictionary<String, Int>()
var results = Array<Int>()
```

## 8. Enumerations

- A way of defining groups of related values in a way that makes them easier to use

```swift
let result = "failure"
let result2 = "failed"
let result3 = "fail"

enum Result {
    case success
    case failure
}

let result4 = Result.failure
```

## 9. Enum Associated Values

- Enum can also store *assocaited* vlaues attached to each case
- This lets you attach additional information to your enums so they can represent more nuanced data

```swift
enum Activity {
    case bored
    case running
    case talking
    case singing
}

enum Activity {
    case bored
    case running(destination: String)
    case talking(topic: String)
    case singing(volume: Int)
}

let talking = Activity.talking(topic: "football)
```

## 10. Enum Raw Values

- Integer raw values count from 0 automatically

```swift
enum Planet: Int {
    case mercury
    case venus
    case earth
    case mars
}

let earth = Planet(rawValue: 2)

enum Planet: Int {
    case mercury = 1
    case venus
    case earth
    case mars
}
