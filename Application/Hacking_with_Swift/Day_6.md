# 100 days of Swift

> 02.12.2023

- Day 6
- [source](https://www.hackingwithswift.com/100/1)

## 1. Creating Basic Closures

- You can create a function and assign it to a variable, call that function usting that variable, and even pass that function into other functions as parameters

```swift
let driving = {
    print("I'm driving in my car")
}

driving()
```

## 2. Accepting Parameters in a Closure

- To make a closure accept parameters, list them inside parentheses just after the opening brace, then write `in` so that Swift knows the main body of the closure is starting
- You don't use parameter labels when running closures

```swift
let driving = { (place: String) in 
    print("I'm going to \(place) in my car")
} 

driving("London")
```

## 3. Returning Values from a Closure

```swift
let drivingWithReturn = { (place: String) -> String in 
    return "I'm going to \(place) in my car"
}

let = message = drivingWithReturn("London")
print(message)
```

## 4. Closures as Parameters

```swift
let driving = {
    print("I'm in driving in my car")
}

func travel(action: () -> Void) {
    print("I'm getting ready to go.")
    action()
    print("I arrived!")
}

travel(action: driving)
```

## 5. Trailing Closure Syntax

- Rather than pass in your closure as a parameter, you pass it directly after the function inside braces

```swift
func travel(action: () -> Void) {
    print("I'm getting ready to go.")
    action()
    print("I'm arrived!")
}

travel {
    print("I'm driving in my car")
}