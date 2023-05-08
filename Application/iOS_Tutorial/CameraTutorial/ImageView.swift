//
//  ImageView.swift
//  CameraTutorial
//  for test
//
//  Created by Nayeon Kim on 2023/05/04.
//

import SwiftUI
import PhotosUI

struct ImageView: View {
    @State private var recentImage: UIImage?
    
    var body: some View {
        VStack {
            if let image = recentImage {
                Image(uiImage: image)
                    .resizable()
                    .scaledToFit()
            } else {
                Text("No image")
            }
        }
        .onAppear {
            PHPhotoLibrary.requestAuthorization(for: .readWrite) { status in
                if status == .authorized {
                    let fetchOptions = PHFetchOptions()
                    fetchOptions.sortDescriptors = [NSSortDescriptor(key: "creationDate", ascending: false)]
                    fetchOptions.fetchLimit = 1
                    
                    let fetchResult = PHAsset.fetchAssets(with: .image, options: fetchOptions)
                    
                    if let asset = fetchResult.firstObject {
                        let requestOptions = PHImageRequestOptions()
                        requestOptions.deliveryMode = .fastFormat
                        requestOptions.isSynchronous = true
                        
                        PHImageManager.default().requestImage(for: asset, targetSize: UIScreen.main.bounds.size, contentMode: .aspectFit, options: requestOptions) { image, _ in
                            recentImage = image
                        }
                    }
                } else {
                    print("error: not authorized.")
                }
            }
        }
    }
}

struct ImageView_Previews: PreviewProvider {
    static var previews: some View {
        ImageView()
//            .preferredColorScheme(.dark)
    }
}
