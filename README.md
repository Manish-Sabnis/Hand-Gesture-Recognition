# Hand Gesture Recognition
## **Author:** Manish Lilesh Sabnis

---

## Objective
This project creates a real-time static hand gesture recognition system using a webcam. It detects a hand in the video feed, tracks its landmarks, and classifies the gesture into one of four categories: 
- Open Palm
- Fist
- Peace (V-sign)
- Thumbs Up

The system shows the recognized gesture live on the video stream.

---

## Technology Justification
- **MediaPipe Hands**:  
I chose MediaPipe Hands because it offers reliable, real-time hand tracking with minimal setup. Instead of spending time collecting and training a custom dataset, MediaPipe provides ready-to-use hand landmarks that are accurate enough for gesture recognition and run smoothly on a standard laptop CPU. This allowed me to focus on the main problem, which is defining the gesture logic.

- **OpenCV**:  
I used OpenCV for video handling and visualization because it’s lightweight and widely used in the industry. It also integrates easily with MediaPipe. Together, these tools provide a practical solution that offers fast performance and is simple for anyone to set up and run.

This combination allows gesture recognition at ~20–30 FPS on a standard laptop, fulfilling the real-time requirement.

---

## Gesture Logic Explanation
Gestures are identified using **relative landmark positions** from MediaPipe:

- **Open Palm**: All five fingers extended (each fingertip above its MCP/base joint).  
- **Fist**: All fingers curled (each fingertip below its MCP/base joint).  
- **Peace Sign**: Index and middle fingers extended, other fingers curled.  
- **Thumbs Up**: Thumb extended outward while all other fingers curled.  

Rules are derived directly from the landmark coordinates, without training a separate classifier.

---

## Setup and Execution Instructions

### 1. Clone the repository
```
git clone https://github.com/Manish-Sabnis/Hand-Gesture-Recognition
cd Hand-Gesture-Recognition
```

### 2. Create a virtual environment (recommended)
```
python3 -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Run the application
```
python src/main.py
```

### Press ESC to quit the webcam window.

---

## Demonstration


https://github.com/user-attachments/assets/74f08ed4-eeb7-4c71-aab3-a07be4f3c307


