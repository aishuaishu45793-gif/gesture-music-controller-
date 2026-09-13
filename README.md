# 🎵 Gesture Music Controller

A computer vision-based music controller that allows users to control music playback using **hand gestures** instead of a keyboard or mouse.

## 📌 Project Overview

**Gesture Music Controller** is an AI/computer-vision project that uses a webcam to detect hand gestures and convert them into music control commands.

The system provides a touch-free way to interact with a music player. Users can perform predefined hand gestures to play, pause, change tracks, adjust volume, and control other music functions.

## ✨ Features

* 🖐️ Real-time hand gesture detection
* 🎵 Play and pause music using gestures
* ⏭️ Skip to the next track
* ⏮️ Go to the previous track
* 🔊 Increase and decrease volume
* 🎚️ Touch-free music control
* 📷 Uses a webcam for gesture input
* ⚡ Real-time gesture processing
* 🤖 Computer vision-based interaction
* 🖥️ Easy-to-use interface

## 🛠️ Technologies Used

* **Python**
* **OpenCV** – Image processing and computer vision
* **MediaPipe** – Hand landmark and gesture detection
* **PyAutoGUI / PyCaw** – System and media control
* **NumPy** – Numerical operations
* **Webcam** – Real-time video input

## 📂 Project Structure

```text
gesture-music-controller/
│
├── main.py
├── requirements.txt
├── README.md
│
├── images/
│   └── screenshots/
│
└── assets/
```

> The exact file structure may vary depending on the implementation.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/aishuaishu45793-gif/gesture-music-controller-.git
```

### 2. Open the project

```bash
cd gesture-music-controller-
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the main Python file:

```bash
python main.py
```

Allow the application to access your webcam when prompted.

Position your hand in front of the camera and perform the supported gestures to control the music.

## 🖐️ Gesture Controls

| Gesture          | Action          |
| ---------------- | --------------- |
| ✋ Open Palm      | Play / Pause    |
| 👉 Right Gesture | Next Track      |
| 👈 Left Gesture  | Previous Track  |
| 👍 Up Gesture    | Increase Volume |
| 👎 Down Gesture  | Decrease Volume |
| ✊ Fist           | Stop / Pause    |

> Gesture mappings can be modified according to the implementation.

## 🔄 How It Works

```text
Webcam
   ↓
Capture Video
   ↓
Hand Detection
   ↓
Hand Landmark Detection
   ↓
Gesture Recognition
   ↓
Gesture-to-Command Mapping
   ↓
Music Player Control
```

The webcam continuously captures video frames. The computer vision system identifies the user's hand and detects important hand landmarks. These landmarks are analyzed to recognize predefined gestures. Once a gesture is identified, the corresponding music-control command is executed.

## 🎯 Project Objectives

* Build a touch-free music control system.
* Apply computer vision to a real-world application.
* Detect and recognize hand gestures in real time.
* Improve human-computer interaction.
* Reduce dependency on traditional input devices.

## 🚀 Future Enhancements

* Add more customizable gestures.
* Support Spotify and other music platforms.
* Add voice-control integration.
* Improve gesture recognition accuracy.
* Add a graphical user interface.
* Support multiple users.
* Add gesture customization.
* Implement machine-learning-based gesture classification.
* Improve performance in low-light environments.

## 💡 Applications

The Gesture Music Controller can be useful for:

* 🎧 Music players
* 🏠 Smart home systems
* 🚗 Touch-free vehicle interfaces
* ♿ Accessibility-focused applications
* 🖥️ Human-computer interaction systems
* 🎮 Interactive multimedia applications

## ⚠️ Requirements

* Python 3.x
* Working webcam
* Windows/macOS/Linux
* Supported music player
* Required Python libraries installed from `requirements.txt`

## 👩‍💻 Author

**Aishwarya**

GitHub: [aishuaishu45793-gif](https://github.com/aishuaishu45793-gif?utm_source=chatgpt.com)

## 📄 License

This project is intended for educational and project-development purposes. You can add an open-source license such as **MIT License** if required.
