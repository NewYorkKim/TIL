# 100 days of Swift

> 02.12.2023

- Day 5
- [source](https://www.hackingwithswift.com/100/1)

## 1. Writing Functions

- Functions let us re-use code
- The most common time when you want the same functionality in many places
- Functions are aslo useful for breaking up code
- Swift lets us build new functions out of existing functions, which is a technique called *function composition*

```swift
func printHelp() {
    let message = """
    Welcome to MyApp!

    Run this app inside a directory of images and MyApp will resize them all into thumbnails
    """

    print(message)
}

printHelp()
```

## 2. Accepting Parameters

- Swift lets you send values to a function that can then be used inside the function to change the way it behaves

```swift
func square(number: Int) {
    print(number * number)
}

square(number: 8)
```

## 3. Returning Values

- You can use the `return` keyword to send a value back if you have one

```swift
func square(number: Int) -> Int {
    return number * number
}

let result = square(number: 8)
print(result)
```

## 4. Parameter Labels

```swift
func sayHello(to name: String) {
    print("Hello, \(name)!")
}

sayHello(to: "Taylor")
```

- The parameter is called `to name`, which means externally it's called `to`, but internally it's called `name`

## 5. Omitting Paramter Labels

```swift
func greet(_ person: String) {
    print("Hello, \(person)!")
}

greet("Taylor")
```

## 6. Default Parameters

- You can give your own parameters a default value just by writing an `=` after its type followed by the default you want to give it

```swift
func greet(_ person: String, nicely: Bool = true) {
    if nicely == true {
        print("Hello, \(person)!")
    } else {
        print("On no, it's \(person) again...")
    }
}
```

## 7. Variadic Functions

- Some functions are *variadic*, which is a fancy way of saying they accept any number of parameters of the same type

```swift
print("Haters", "gonna", "hate")

func square(numbers: Int...) {
    for number in numbers {
        print("\(number) squared is \(number * number)")
    }
}

square(numbers: 1, 2, 3, 4, 5)
```

## 8. Writing Throwing Functions

- Swift lets us throw erros from functions by marking `throw` before their return type, then using `throw` keyword when something goes wrong

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
```

## 9. Running Throwing Functions

- `do` starts a section of code that might cause problems
- `try` is used before every function that might throw an error
- `catch` lets you handle errors gracefully

```swift
do {
    try checkPassword("password")
    print("That password is good!")
} catch {
    print(
        "You can't use that password.")
}
```

## 10. Inout Parameters

- You can pass in one or more parameters as `inout`, which means they can be changed insdie your function, and those changes reflect in the original value outside the function

```swift
func doubleInPlace(number: inout Int) {
    number *= 2
}

var myNum = 10
doubleInPlace(number: &myNum)