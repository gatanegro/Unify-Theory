// VR AI Assistant for Interactive ChatGPT in VR Math Lab
// Uses Three.js + WebXR + WebSocket for real-time AI interaction

import * as THREE from 'three';
import { VRButton } from 'three/examples/jsm/webxr/VRButton.js';

let scene, camera, renderer, chatBox;
let ws;

// Initialize Three.js Scene
function init() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 5;

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.xr.enabled = true;
    document.body.appendChild(renderer.domElement);
    document.body.appendChild(VRButton.createButton(renderer));

    // Create Chat Box for AI Responses
    let chatGeometry = new THREE.PlaneGeometry(3, 1);
    let chatMaterial = new THREE.MeshBasicMaterial({ color: 0x000000, side: THREE.DoubleSide });
    chatBox = new THREE.Mesh(chatGeometry, chatMaterial);
    chatBox.position.set(0, 2, -3);
    scene.add(chatBox);

    // Connect to AI WebSocket Server
    ws = new WebSocket('ws://localhost:8765');
    ws.onmessage = (event) => updateChat(event.data);
}

// Update ChatGPT Response in VR
function updateChat(text) {
    let canvas = document.createElement('canvas');
    let ctx = canvas.getContext('2d');
    canvas.width = 512;
    canvas.height = 128;
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = 'black';
    ctx.font = '20px Arial';
    ctx.fillText(text, 10, 50);
    let texture = new THREE.CanvasTexture(canvas);
    chatBox.material.map = texture;
    chatBox.material.needsUpdate = true;
}

// Animation Loop
function animate() {
    renderer.setAnimationLoop(() => {
        renderer.render(scene, camera);
    });
}

// Run Everything
init();
animate();