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
    @State private var AccelerationData = []
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
                        AccelerationData.append(attitude.y)
                        flag = true
                    } else {
                        if flag == true {
                            pitchingCount += 1
                            maximum = AccelerationData[AccelerationData.count-1] as! Double
                            flag = false
                        }
                        
                        AccelerationData = []
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
