# TypeScript로 블록체인 만들기: Day 09

> 2022/07/05

- source: [TypeScript로 블록체인 만들기](https://nomadcoders.co/typescript-for-beginners)

`TypeScript` `Blockchain` `VSCode`



## Classes and Interfaces

##### Polymorphism

- 다형성: 다른 모양의 코드를 가질 수 있게 해주는 것
  - ➡ **generic**



```typescript
interface SStorage<T> {
    [key: string]: T
}

class LocalStorage<T> {
    private storage: SStorage<T> = {}
    set(key:string, value:T){
        this.storage[key] = value
    }
    remove(key:string){
        delete this.storage[key]
    }
    get(key:string): T {
        return this.storage[key]
    }
    clear(){
        this.storage = {}
    }
}

const stringsStorage = new LocalStorage<string>()

stringsStorage.get('key')
stringsStorage.set("hello", "how are you?")

const booleansStorage = new LocalStorage<boolean>()

booleansStorage.get("xxx")
booleansStorage.set("hello", true)
```

