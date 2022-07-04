# TypeScript로 블록체인 만들기: Day 08

> 2022/07/04

- source: [TypeScript로 블록체인 만들기](https://nomadcoders.co/typescript-for-beginners)

`TypeScript` `Blockchain` `VSCode`



## Functions

##### Interfaces

```typescript
type Player = {
    nickname: string,
    healthBar: number
}

const user: Player = {
    nickname: "user",
    healthBar: 10
}

type Food = string

const kimchi: Food = "delicious"
```

```typescript
type Team = "red" | "blue" | "yellow"  // 특정 값으로 제한
type Helath = 1 | 5 | 10

type Player = {
    nickname: string,
    team: Team
    health: Health
}

const user: Player = {
    nickname: "user",
    // team: "pink"  // 허용 ❌
    team: "yellow",
    health: 10
}
```



- 인터페이스
  - **오브젝트**의 모양을 특정할 때 사용 (`type`, `interface`)
  - 클래스를 다루는 것과 유사
  - property 축적 가능

```typescript
type Team = "red" | "blue" | "yellow"  
type Helath = 1 | 5 | 10

interface Player {
    nickname: string,
    team: Team,
    health: Health
}

const user: Player = {
    nickname: "user",
    team: "yellow",
    health: 10
}
```

```typescript
interface User {
    name: string
}

interface Player extends User {    
}

const user: Player = {
    name: "user"
}
```

```typescript
interface User {
    name: string
}

type Player = User & {
}

const user: Player = {
    name: "user"
}
```

```typescript
interface User {
    readonly name: string
}

interface Player extends User {    
}

const user: Player = {
    name: "user"
}

user.name = "lalalala"  // readonly ➡ 수정 ❌
```

```typescript
interface User {
    name: string
}

interface User {
    lastName: string
}

interface User {
    health: number
}

const user: User = {
    name: "user",
    lastName: "last",
    health: 10
}
```



- vs. 추상 클래스
  - 표준화된 property와 메소드를 갖도록 해주는 청사진을 만들기 위해 사용
  - 자바스크립트: 추상 클래스 개념 ❌ ➡ 일반 클래스로 변환

```typescript
abstract class User {
    constructor (
        protected firstName: string,
        protected lastName: string
    ) {}
    abstract sayHi(name: string): string
    abstract fullName(): string
}

class Player extends User {
    fullName(){
        return `${this.firstName} ${this.lastName}`
    }
    sayHi(name: string){
        return `Hello ${name}. My name is ${this.fullName()}`
    }
}
```

- 인터페이스
  - 파일을 보다 가볍게
  - 인터페이스 축적 가능
  - 타입으로 사용 가능

```typescript
interface User {
    firstName: string,
    lastName: string,
    sayHi(name: string): string,
    fullName(): string
}

interface Human {
    health: number
}

class Player implements User, Human {
    constructor(
    	public firstName: string,
        public lastName: string,
        public health: number
    ){}
    fullName(){
        return `${this.firstName} ${this.lastName}`
    }
    sayHi(name: string){
        return `Hello ${name}. My name is ${this.fullName()}`
    }
}

function makeUser(user: User) {
    return "hi"
}

makeUser({
    firstName: "user",
    lastName: "last",
    fullName: () => "xx",
    sayHi: (name) => "string"
})
```



## Assignment 06

- Quiz: `8/8`

