# 100 days of Swift

> 02.11.2023

- Day 4
- [source](https://www.hackingwithswift.com/100/1)

## 1. For Loops

- Loop over arrays and ranges, and each time the loop goes around it will pull out one item and assign to a constant

```swift
let count = 1...10

for number in count {
    print("Number is \(number)")
}

let albums = ["Red", "1989", "Reputation"]

for album in albums {
    print("\(album) is on Apple Music")
}

print("Players gonna ")

for _ in 1...5 {
    print("play")
}
```

## 2. While Loops

- Give it a condition to check, and its loop code will go around and around until the condition fails

```swift
var number = 1

while number <= 20 {
    print(number)
    number += 1
}

print("Ready or not, here I come!")
```

## 3. Repeat Loops

- It's identical to a `while` loop except the condition to check comes at the end

```swift
var number = 1

repeat {
    print(number)
    number += 1
} while number <= 20

print("Ready or not, here I come!")

while false {
    print("This is false")
}

repeat {
    print("This is false")
} while false
```

## 4. Exiting Loops

- You can exit a loop at any time using the `break` keyword

```swift
var countDown = 10

while countDown >= 0 {
    print(countDown)
    countDown -= 1
}

print("Blast off!")

while countDown >= {
    print(countDown)

    if countDown == 4 {
        print("I'm bored. Let's go now!")
        break
    }
    countDown -= 1
}
```

## 5. Exiting Multiple Loops

```swift
for i in 1...10 {
    for j in 1...10 {
        let product = i * j
        print("\(i) * \(j) is \(product)")
    }
}

outerLoop: for i in 1...10 {
    for j in 1...10 {
        let product = i * j
        print("\(i) * \(j) is \(product)")
    }
}

outerLoop: for i in 1...10 {
    for j in 1...10 {
        let product = i * j
        print("\(i) * \(j) is \(product)")

        if product == 50 {
            print("It's a bullseye!")
            break outerLoop
        }
    }
}
```

## 6. Skipping Items

- If you just want to skip the current item and continue on to the next one, you should use `countinue`

```swift
for i in 1...10 {
    if i % 2 == 1{
        continue
    }
    print(i)
}
```

## 7. Infinite Loops

```swift
var counter = 0

while true {
    print(" ")
    counter += 1

    if counter == 273 {
        break
    }
}
```