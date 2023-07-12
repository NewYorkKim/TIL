//
//  MessageBubble.swift
//  MessageTutorial
//
//  Created by Nayeon Kim on 2023/07/12.
//

import SwiftUI

struct MessageBubble: View {
    @State var user = UIDevice.current.identifierForVendor!.uuidString
    var message: Message
    
    var body: some View {
        VStack(alignment: message.user != user ? .leading : .trailing) {
            HStack {
                Text(message.text)
                    .padding(8)
                    .background(message.user != user ? Color(.systemGray6) : Color.blue)
                    .foregroundColor(message.user != user ? .black : .white)
                    .cornerRadius(10)
            }
            .frame(maxWidth: 300, alignment: message.user != user ? .leading : .trailing)
            
            Text("\(message.timestamp.formatted(.dateTime.hour().minute()))")
                .font(.caption2)
                .foregroundColor(.gray)
                .padding(message.user != user ? .leading : .trailing, 4)
        }
        .frame(maxWidth: .infinity, alignment: message.user != user ? .leading : .trailing)
        .padding(message.user != user ? .leading : .trailing)
        .padding(.horizontal, 12)
    }
}

struct MessageBubble_Previews: PreviewProvider {
    static var previews: some View {
        MessageBubble(message: Message(id: "1", text: "Hello", user: UIDevice.current.identifierForVendor!.uuidString, timestamp: Date()))
    }
}
