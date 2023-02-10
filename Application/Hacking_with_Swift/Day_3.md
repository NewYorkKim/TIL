# 100 days of Swift

> 02.10.2023

- Day 3
- [source](https://www.hackingwithswift.com/100/1)

## 1. Arithmetic Operators

```swift
let firstScore = 12
let secondScore = 4

let total = firstScore + secondScore
let difference = firstScore - secondScore

let product = firstScore * secondScore
let divided = firstScore / secondScore

let remainder = 12 % secondScore
```

## 2. Operaotr Overloading

```swift
let meaningOfLife = 42
let doubleMeaning = 42 + 42

let fakers = "Fakers gonna "
let action = fakers + "fake"

let firstHalf = ["John", "Paul"]
let secondHalf = ["George", "Ringo"]
let beatles = firstHalf + secondHalf
```

## 3. Compound assignment operators

- Shorthand operators that combine one operator with an assignment

```swift
var score = 95
score -= 5

var quote = "The rain in Spain falls mainly on the "
quote += "Spaniards"
```

## 4. Comparison Operators

```swift
let fistScore = 6
let secondScore = 4

firstScore == secondScore
firstScore != secondScore

firstScore < secondScore
firstScore >= secondScore

"Taylor" <= "Swift"
```

## 5. Conditions

```swift
let firstCard = 11
let secondCard = 10

if firstCard + secondCard == 2 {
    print("Aces - lucky!")
} else if firstCard + secondCard == 21 {
    print("Blackjack!")
} else {
    print("Regular cards")
}
```

## 6. Combining Conditions

- `&&`: "and"
- `||`: "or"

```swift
let age1 = 12
let age2 = 21

if age1 > 18 && age2 > 18 {
    print("Both are over 18")
}

if age1 > 18 || age2 > 18 {
    print("At least one is over 18")
}
```

## 7. The Ternary Operator

- It works with three values at once
    1. It checks a condition specified in the first value
    2. If it's true returns the second value
    3. But, if it's false returns the third value

```swift
let firstCard = 11
let secondCard = 10
print(firstCard == secondCard ? "Cards are the same" : "Cards are different")

if firstCard == secondCard {
    print("Cards are the same")
} else {
    print("Cards are different")
}
```

## 8. Switch Statements

- `default` is required because Swift makes sure you cover all possible cases so that no eventually is missed off
- If you want to execution to continue on to the next case, use the `fallthough`

```swift
let weather = "sunny"

switch weather {
    case "rain":
        print("Bring an umbrella")
    case "snow":
        print("Wrap up warm")
    case "sunny":
        print("Wear sunscreen")
        fallthrough
    default:
        print("Enjoy your day!")
}
```

## 9. Range Operators

- `..<`: The half-open range operator creates ranges up to but excluding the final value
- `...`: The closed range operator creates ranges up to and including the final value

```swift
let score = 85

switch score {
    case 0..<50:
        print("You failed badly.")
    case 50..<85:
        print("You did OK.")
    default:
        print("You did great!")
}
```