//
//  ContentView.swift
//  CoreMotionTutorial
//
//  Created by Nayeon Kim on 2023/08/17.
//

import SwiftUI
import CoreMotion

struct ContentView: View {
    @State private var motionManager = CMMotionManager()
    @State private var pitchingCount = 0
    @State private var maximum = 0.0
    @State private var vectorData: [Double] = []
    @State private var flag = false
    
    var body: some View {
        VStack {
            Spacer()
            
            Text("투구 수")
                .font(.headline)
            Text("\(pitchingCount)")
            
            Spacer()
            
            Text("최대")
                .font(.headline)
            Text("\(maximum)")
            
            Spacer()
            
        }
        .padding()
        .onAppear {
            startMotionUpdates()
        }
    }
    
    func startMotionUpdates() {
        if motionManager.isAccelerometerAvailable {
            motionManager.accelerometerUpdateInterval = 1
            
            motionManager.startDeviceMotionUpdates(to: .main) { data, error in
                if let attitude = data?.userAcceleration {
                    print(pitchingCount, attitude.y)
                    
                    if attitude.y > 10 {
                        let vector = sqrt(pow(attitude.x, 2) + pow(attitude.y, 2) + pow(attitude.z, 2))
                        vectorData.append(vector)
                        flag = true
                    } else {
                        if flag == true {
                            pitchingCount += 1
                            maximum = vectorData[vectorData.count-1]
                            flag = false
                        }
                        
                        vectorData = []
                    }
                }
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
