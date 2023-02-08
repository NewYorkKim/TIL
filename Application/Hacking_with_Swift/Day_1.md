# 100 days of Swift

> 02.08.2023

- Day 1
- [source](https://www.hackingwithswift.com/100/1)

## 1. Variables

 - Places where you can store program data
- they can *vary* - you can change their values freely
- We don't need `var` the second time because the variable has already been created

```swift
var str = "Hello, playground"

str = "Goodbye"
```

## 2. String and Integers

- A type-safe language: Every variable must be of one specific type
- `Int`: Short for "integer"
    - If you have large numbers, Swift lets you use **underscores** as thousands seperators

```swift
var age = 38
var population = 8_000_000
```

## 3. Multi-line Strings

- Start and end with three double quote marks
- If you only want multi-line strings to format your code neatly, and you don't want those line breaks to actually be in your string, end each line with a `\`

```swift
var str1 = """
This goes
over multiple
lines
"""

var str2 = """
This goes \
over multiple \
lines
"""
```

## 4. Doubles and Booleans

- Double: "double-precision floating-point number"
- Boolean: true or false

```swift
var pi = 3.141
var awesome = true
```

## 5. String Interpolation

- The ability to place variables inside your strings

```swift
var score = 85
var str = "Your score was \(score)"
var results = "The test results are here: \(str)"
```

## 6. Constants

- `let`
- Values that can be set once and never again

```swift
let taylor = "swift"
```

## 7. Type Annotations

- Type Inference
- But, you can provide explicit types if you want

```swift
let str = "Hello, playground"

let album: String = "Reputation"
let year: Int = 1989
let height: Double = 1.78
let taylorRocks: Bool = true
```

- Why does Swift have type annotations?
    1. Swift can't figure out what type should be used
    2. You want Swift to use a different type from its default
    3. You don't want to assign a value just yet

```swift
var percentage: Double = 99
var name: String
```