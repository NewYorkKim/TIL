//
//  ContentView.swift
//  MessageTutorial
//
//  Created by Nayeon Kim on 2023/07/11.
//

import SwiftUI
import MessageUI

struct ContentView: View {
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("Hello, world!")
        }
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
