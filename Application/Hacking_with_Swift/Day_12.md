# 100 days of Swift

> 02.17.2023

- Day 12
- [source](https://www.hackingwithswift.com/100/1)

## 1. Handling Mssing Data

- *optionals*

```swift
var age: Int? = nil

age = 38
```

## 2. Unwrapping Optionals

```swift
var name: String? = nil

if let unwrapped = name {
    print("\(unwrapped.count) letters")
} else {
    print("Missing name.")
}
```

## 3. Unwrapping with Guard

```swift
func greet(_ name: String?) {
    guard let unwrapped = name else {
        print("You didn't provide a name!")
        return
    }

    print("Hello, \(unwrapped)!")
}
```

## 4. Force Unwrapping

```swift
let str = "5"
let num = Int(str)

let num = Int(str)!
```

## 5. Implicity Unwrapped Optionals

- Implicity unwrapped optionals exist because sometimes a variable will start life as nil, but will always have a value before you need to use it

```swift
let age: Int! = nil
```

## 6. Nil Coalescing

- The nil coalescing operator unwraps an optionals and returns the value inside if there is one

```swift
func username(for id: Int) -> String? {
    if id == 1 {
        return "Talyor Swift"
    } else {
        return nil
    }
}

let user = username(for: 15) ?? "Anonymous"
```

## 7. Optional Chaining

- If you want access something like `a.b.c` and `b` is optional, you can write a question mark after it to enable *optional chaining*: `a.b?.c`

```swift
let names = ["John", "Paul", "George", "Ringo"]

let beatle = name.first?.uppercased()
```

## 8. Optional Try

```swift
enum PasswordError: Error {
    case obvious
}

func checkPassword(_ password: String) throws -> Bool {
    if password == "password" {
        throw PasswordError.obvious
    }

    return true
}

do {
    try checkPassword("password")
    print("That password is good!")
} catch {
    print("You can't use that password.")
}

if let result = try? checkPassword("password") {
    print("Result was \(result)")
} else {
    print("D'oh.")
}

try! checkPassword("sekrit")
print("OK!")
```

## 9. Failable Initializers

```swift
struct Person {
    var id: String

    init?(id: String) {
        if id.count == 9 {
            self.id = id
        } else {
            return nil
        }
    }
}
```

## 10. Typecasting

```swift
class = Animal { }
class Fish: Animal { }

class Dog: Animal {
    func makeNoise() {
        print("Woof!")
    }
}

let pets = [Fish(), Dog(), Fish(), Dog()]

for pet in pets {
    if let dog = pet as? Dog {
        dog.makeNoise()
    }
}
```