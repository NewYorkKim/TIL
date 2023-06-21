//
//  ViewController.swift
//  ARTutorial
//
//  Created by Nayeon Kim on 2023/06/21.
//

import UIKit
import SceneKit
import ARKit

class ViewController: UIViewController, ARSCNViewDelegate {

    @IBOutlet var sceneView: ARSCNView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Set the view's delegate
        sceneView.delegate = self
        
        // Show statistics such as fps and timing information
        sceneView.showsStatistics = true
        
        // Create a new scene
        let scene = SCNScene()
        
        // Set the scene to the view
        sceneView.scene = scene
        
        makeEarth()
//        makeNickname()
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        // Create a session configuration
        let configuration = ARWorldTrackingConfiguration()
        configuration.frameSemantics.insert(.personSegmentation)

        // Run the view's session
        sceneView.session.run(configuration)
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        
        // Pause the view's session
        sceneView.session.pause()
    }

    // MARK: - ARSCNViewDelegate
    
/*
    // Override to create and configure nodes for anchors added to the view's session.
    func renderer(_ renderer: SCNSceneRenderer, nodeFor anchor: ARAnchor) -> SCNNode? {
        let node = SCNNode()
     
        return node
    }
*/
    
    func session(_ session: ARSession, didFailWithError error: Error) {
        // Present an error message to the user
        
    }
    
    func sessionWasInterrupted(_ session: ARSession) {
        // Inform the user that the session has been interrupted, for example, by presenting an overlay
        
    }
    
    func sessionInterruptionEnded(_ session: ARSession) {
        // Reset tracking and/or remove existing anchors if consistent tracking is required
        
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        if let location = touches.first?.location(in: self.view), let hit = sceneView.hitTest(location).first {
            let increaseSize = SCNAction.scale(by: 1.2, duration: 1)
            let decreaseSize = SCNAction.scale(by: 0.8, duration: 1)
            let sizeSequence = SCNAction.sequence([increaseSize, decreaseSize])
            
            hit.node.runAction(sizeSequence)
        }
    }
    
    func makeEarth() {
        let earth = SCNSphere(radius: 0.2)
        
        let material = SCNMaterial()
        material.diffuse.contents = UIImage(named: "art.scnassets/earthmap.jpg")
        
        earth.materials = [material]
        
        let node = SCNNode(geometry: earth)
        node.position = SCNVector3(x: 0, y: 0, z: -1)
        
        sceneView.scene.rootNode.addChildNode(node)
        node.addChildNode(makeNickname())
        
        addAnimation(node: node)
    }
    
    func makeNickname() -> SCNNode{
        let text = SCNText(string: "NewYork", extrusionDepth: 2)
        
        let material = SCNMaterial()
        material.diffuse.contents = UIColor.blue
        
        text.materials = [material]
        
        let node = SCNNode(geometry: text)
        node.scale = SCNVector3(0.02, 0.02, 0.02)
        node.position = SCNVector3(x: -0.5, y: 0.2, z: 0)
        
        return node
    }
    
    func addAnimation(node: SCNNode) {
        let rotateOneTime = SCNAction.rotateBy(x: 0, y: 0.8, z: 0, duration: 5)
        let actionForever = SCNAction.repeatForever(rotateOneTime)
        
        node.runAction(actionForever)
    }
}
