# 100 days of Swift

> 02.15.2023

- Day 10
- [source](https://www.hackingwithswift.com/100/1)

## 1. Creating Your Own Classes

- Classes never come with a memberwise initializer
- If you have properties in your class, you must always create your own initializer

```swift
class Dog {
    var name: String
    var breed: String

    init(name: String, breed: String) {
        self.name = name
        self.breed = breed
    }
}

let poppy = Dog(name: "Poppy", breed: "Poodle")
```

## 2. Class Inheritance

- You can create a class based on an existing class – it inherits all the properties and methods of the original class, and can add itw own on top
- *class inheritance* or *subclassing*

```swift
class Dog {
    var name: String
    var breed: String

    init(name: String, breed: String) {
        self.name = name
        self.breed = breed
    }
}

class Poodle: Dog {
    init(name: String) {
        super.init(name: name, breed: "Poodle")
    }
}
```

## 3. Overriding Methods

- Child classes can replace parent methods with their own implementations – a process known as *overriding*

```swift
class Dog {
    func makeNoise() {
        print("Woof!")
    }
}

class Poodle: Dog {
    override func makeNoise() {
        print("Yip!")
    }
}

let poppy = Poodle()
poppy.makeNoise()
```

## 4. Final Classes

- When you declare a class as being `final`, no other class can inherit from it

```swift
final class Dog {
    var name: String
    var breed: String

    init(name: String, breed: String) {
        self.name = name
        self.breed = breed
    }
}
```

## 5. Copying Objects

- When you copy a struct, both the original and the copy are different things
- When you copy a class, both the original and the copy point to the same thing, so changing one does change the other

```swift
class Singer {
    var name = "Taylor Swift"
}

var singer = Singer()
print(singer.name)

var singerCopy = singer
singerCopy.name = "Justin Bieber"

print(singer.name)

struct Singer {
    var name = "Taylor Swift"
}
```

## 6. Deinitializers

- Classes can have *deinitializers* – code that gets run when an instance of a class is destroyed

```swift
class Person {
    var name = "John Doe"

    init() {
        print("\(name) is alive!")
    }

    func printGreeting() {
        print("Hello, I'm \(name)")
    }

    deinit {
        print("\(name) is no more!")
    }
}

for _ in 1...3 {
    let person = Person()
    person.printGreeting()
}
```

## 7. Mutability

- If you have a constant class with a variable property, that propert can be changed
- Because of this, classes don't need the `mutating` keyword with methods that change properties

```swift
class Singer {
    var name = "Taylor Swift"
}

let taylor = Singer()
taylor.name = "Ed Sheeran"
print(taylor.name)

class Singer {
    let name = "Taylor Swift"
}
```