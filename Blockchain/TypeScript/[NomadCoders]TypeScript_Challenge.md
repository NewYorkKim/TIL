# TypeScript로 블록체인 만들기: Day 11

> 2022/07/07

- source: [TypeScript로 블록체인 만들기](https://nomadcoders.co/typescript-for-beginners)

`TypeScript` `Blockchain` `VSCode`



## TypeScript Blockchain

##### Targets

- `tsconfig.json`: VSCode ➡ 타입스크립트로 작업할 것을 인식 ➡ 자동완성기능 제공

  - `include`: 타입스크립트 파일이 어디에 위치하는지

  - `outDir`: 자바스크립트 파일이 생성될 디렉토리 지정

    ![image-20220708000250986](C:\Users\NY\TIL\Blockchain\TypeScript\[NomadCoders]TypeScript_Challenge.assets\image-20220708000250986.png)

    ![image-20220708000307333](C:\Users\NY\TIL\Blockchain\TypeScript\[NomadCoders]TypeScript_Challenge.assets\image-20220708000307333.png)

    ![image-20220708000343803](C:\Users\NY\TIL\Blockchain\TypeScript\[NomadCoders]TypeScript_Challenge.assets\image-20220708000343803.png)

    

  - `target`: 타입스크립트를 어떤 버전의 자바스크립트로 컴파일할지

    - **ES3**: `const`&화살표 함수 존재하지 않음
    - **ES6**: 가장 이상적

    ![image-20220708000939483](C:\Users\NY\TIL\Blockchain\TypeScript\[NomadCoders]TypeScript_Challenge.assets\image-20220708000939483.png)

