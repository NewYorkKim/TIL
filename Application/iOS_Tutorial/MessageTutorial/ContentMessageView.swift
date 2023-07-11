//
//  ContentMessageView.swift
//  MessageTutorial
//
//  Created by Nayeon Kim on 2023/07/11.
//

import SwiftUI

struct ContentMessageView: View {
    var contentMessage: String
    var isCurrentUser: Bool
    
    var body: some View {
        Text(contentMessage)
            .padding(10)
            .foregroundColor(isCurrentUser ? .white : .black)
            .background(isCurrentUser ? .blue: Color(UIColor(red: 116/255, green: 116/255, blue: 128/255, alpha: 0.08)))
            .cornerRadius(10)
    }
}

struct ContentMessageView_Previews: PreviewProvider {
    static var previews: some View {
        ContentMessageView(contentMessage: "Hello!", isCurrentUser: false)
    }
}
