# 100 days of Swift

> 02.12.2023

- Day 7
- [source](https://www.hackingwithswift.com/100/1)

## 1. Using Closures as Parameters When They Accept Parameters

```swift
func travel(action: (String) -> Void) {
    print("I'm getting ready to go.")
    action("London")
    print("I arrived!")
}

travel { (place: String) in
    print("I'm going to \(place) in my car")
}
```

## 2. Using Closures as Parameters When They Return Values

```swift
func travel(action: (String) -> String) {
    print("I'm getting ready to go.")
    let description = action("London")
    print(description)
    print("I arrived!")
}

travel { (place: String) -> String in 
    return "I'm going to \(place) in my car"
}
```

## 3. Shorthand Parameter Names

```swift
func travel(action: (String) -> String) {
    print("I'm getting ready to go.")
    let description = action("London")
    print(description)
    print("I arrived!")
}

travel { (place: String) -> String in
    return "I'm going to \(place) in my car"
}

travel { place -> String in
    return "I'm going to \(place) in my car"
}

travel { place in
    return "I'm going to \(place) in my car"
}

travel { place in
    "I'm going to \(place) in my car"
}

travel {
    "I'm going to \($0) in my car"
}
```

## 4. Closures with Multiple Parameters

```swift
func travel(action: (String, Int) -> String) {
    print("I'm getting ready to go.")
    let description = action("London", 60)
    print(description)
    print("I arrived!")
}

travel {
    "I'm going to \($0) at \($1) miles per hour."
}
```

## 5. Returning Closures from Functions

```swift
func travel() -> (String) -> Void {
    return {
        print("I'm going to \($0)")
    }
}

let result = travel()
result("London")

let result2 = travel()("London")
```

## 6. Capturing Values

- If you use any external values inside your closure, Swift *captures* them – stores them alongside the closure, so they can be modified even if they don't exist any more

```swift
func travel() -> (String) -> Void {
    return {
        print("I'm going to \($0)")
    }
}

let result = travel()
result("London")

func travel() -> (String) -> Void {
    var counter = 1

    return {
        print("\(counter). I'm going to \($0)")
        counter += 1
    }
}

result("London")
result("London")
result("London")
```