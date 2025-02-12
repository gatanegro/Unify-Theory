// VR Prototype for Recursive Bubble Field with Dynamic Oscillations
// Using Three.js & WebXR for Immersive Visualization

import * as THREE from 'three';
import { VRButton } from 'three/examples/jsm/webxr/VRButton.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

let scene, camera, renderer;
let bubbles = [];
const numBubbles = 20;
const timeFactor = 0.05;

// Initialize Three.js Scene
function init() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 10;
    
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.xr.enabled = true;
    document.body.appendChild(renderer.domElement);
    document.body.appendChild(VRButton.createButton(renderer));

    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    
    // Create Bubble Nodes
    for (let i = 0; i < numBubbles; i++) {
        let geometry = new THREE.SphereGeometry(0.5, 32, 32);
        let material = new THREE.MeshStandardMaterial({ color: new THREE.Color(Math.random(), Math.random(), Math.random()), emissive: 0x111111 });
        let bubble = new THREE.Mesh(geometry, material);
        
        let angle = (i / numBubbles) * Math.PI * 2;
        bubble.position.set(Math.cos(angle) * 5, Math.sin(angle) * 5, Math.sin(angle) * 3);
        scene.add(bubble);
        bubbles.push(bubble);
    }

    // Lighting
    const light = new THREE.PointLight(0xffffff, 1, 100);
    light.position.set(10, 10, 10);
    scene.add(light);
}

// Animation Loop
function animate() {
    renderer.setAnimationLoop(() => {
        let time = performance.now() * timeFactor;
        bubbles.forEach((bubble, index) => {
            let scale = Math.sin(time + index * 0.2) * 0.3 + 1.0;
            bubble.scale.set(scale, scale, scale);
        });

        renderer.render(scene, camera);
    });
}

// Run Everything
init();
animate();