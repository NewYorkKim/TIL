# PhotoKit

- iOS 및 macOS에서 Photo 앱에 대한 **사진 편집** 확장 기능 구축을 지원하는 클래스를 제공
- iOS, macOS 및 tvOS에서 Photo 앱에서 관리하는 사진 및 비디오 데이터에 **직접 접근**할 수 있음

![overview](https://docs-assets.developer.apple.com/published/b57f722288/rendered2x-1655840094.png)

## PHPhotoLibrary

- 앱의 사용자가 가진 라이브러리에 대해 <U>접근 권한 및 변경</U> 등을 관리하는 객체
- 사진의 사용을 위한 유저의 권한 획득 
- Asset 및 Collection 변경
- 라이브러리가 변경될 때, 등록된 메시지 전송

## PHAsset

- 이미지와 비디오 그리고 iPhone의 Live Photo을 대표하는 타입
- PHAsset의 메소드를 이용 ➡️ 원하는 Asset을 Fetching
- `Asset`: 메타 데이터, 객체 변경 ❌
    - `PHImageManager`: 어떤 썸네일 이미지를 가져와야 할 경우
    - `PHAssetChangeRequest`: 데이터를 편집해야 할 경우

## PHCollection

- PHAssetCollection과 PHCollectionList의 abstract superclass
- 직접적으로 생성 작업 ❌
    - `PHAssetCollection`
    - `PHCollectionList`

## PHCollectionList

- Asset의 모음
- `fetchCollection(in:options:)`: PHCollectionList의 데이터를 가져와야 할 경우
- `fetchTopLevelUserCollection(with:)`: 어떤 폴더의 최상위 폴더를 찾고 싶은 경우
- 변경 ❌
    - 폴더 생성, 삭제, 재배치, 업데이트 ➡️ PHCollectionListChangeRequest 객체를 photo library change block에 생성

## PHAssetCollection

- Asset의 Group
- 직접 참조 ❌
    `fetchAssets(:options:)`의 메소드 사용

## PHFetchResult

- Photos의 Fetch 작업으로부터 반환된 Asset 또는 Collections의 집단
- NSArray에서 사용하는 것과 동일하게 접근하여 데이터 사용 가능

## PHFetchOptions

- 데이터를 가져오기 위해 필터링, 정렬 등 어떤 옵션을 줄 수 있는 객체
- 원하는 데이터만 뽑아내거나 정렬할 수 있음
    - `predicate`, `sortDescriptors` 