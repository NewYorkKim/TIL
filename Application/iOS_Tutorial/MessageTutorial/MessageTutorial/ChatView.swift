//
//  ChatView.swift
//  MessageTutorial
//
//  Created by Nayeon Kim on 2023/07/11.
//

import SwiftUI

struct ChatView: View {
    @StateObject var messageManager = MessageManager()
    
    var body: some View {
        VStack {
            ScrollViewReader { proxy in
                ScrollView {
                    ForEach(messageManager.messages, id: \.id) { message in
                        MessageBubble(message: message)
                    }
                }
                .padding(.top, 8)
                .onChange(of: messageManager.lastMessageId) { id in
                    withAnimation {
                        proxy.scrollTo(id, anchor: .bottom)
                    }
                }
            }
            
            MessageField()
                .environmentObject(messageManager)
        }
    }
}

struct ChatView_Previews: PreviewProvider {
    static var previews: some View {
        ChatView()
    }
}
