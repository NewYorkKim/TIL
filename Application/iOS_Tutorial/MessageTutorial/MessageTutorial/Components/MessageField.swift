//
//  MessageField.swift
//  MessageTutorial
//
//  Created by Nayeon Kim on 2023/07/12.
//

import SwiftUI

struct MessageField: View {
    @EnvironmentObject var messageManager: MessageManager
    @State private var message = ""
    
    var body: some View {
        ZStack(alignment: .trailing) {
            TextField("Type a message", text: $message)
                .padding(12)
                .padding(.trailing, 48)
                .background(Color(.systemGroupedBackground))
                .clipShape(Capsule())
                .font(.subheadline)
            
            Button {
                messageManager.sendMessage(text: message)
                message = ""
            } label: {
                Text("Send")
                    .fontWeight(.semibold)
            }
            .padding(.horizontal)
        }
        .padding()
    }
}

struct MessageField_Previews: PreviewProvider {
    static var previews: some View {
        MessageField()
            .environmentObject(MessageManager())
    }
}
