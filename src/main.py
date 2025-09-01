import cv2
import mediapipe as mp
import time
from collections import deque

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


def is_finger_up(landmarks, tip_id, mcp_id):
    return landmarks[tip_id].y < landmarks[mcp_id].y

def is_thumb_up(landmarks, hand_label):
    if hand_label == "Right":
        return landmarks[4].x < landmarks[3].x
    else: 
        return landmarks[4].x > landmarks[3].x

def detect_gesture(landmarks, hand_label):
    index_up = is_finger_up(landmarks, 8, 5)
    middle_up = is_finger_up(landmarks, 12, 9)
    ring_up = is_finger_up(landmarks, 16, 13)
    pinky_up = is_finger_up(landmarks, 20, 17)
    thumb_up = is_thumb_up(landmarks, hand_label)

    if index_up and middle_up and ring_up and pinky_up and thumb_up:
        return "Open Palm"
    elif not index_up and not middle_up and not ring_up and not pinky_up and not thumb_up:
        return "Fist"
    elif index_up and middle_up and not ring_up and not pinky_up:
        return "Peace"
    elif thumb_up and not index_up and not middle_up and not ring_up and not pinky_up:
        return "Thumbs Up"
    else:
        return "Unknown"


cap = cv2.VideoCapture(0)

prev_time = time.time()
fps_buffer = deque(maxlen=10)  

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip and convert to RGB
        image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)

        # Back to BGR for display
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        gesture_name = "No Hand"

        if results.multi_hand_landmarks:
            for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                hand_label = results.multi_handedness[idx].classification[0].label
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )
                gesture_name = detect_gesture(hand_landmarks.landmark, hand_label)

        # FPS calculation (moving average)
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if prev_time else 0
        prev_time = curr_time
        fps_buffer.append(fps)
        fps_display = int(sum(fps_buffer) / len(fps_buffer))

        # Overlay gesture and FPS
        cv2.putText(image, f"Gesture: {gesture_name}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(image, f"FPS: {fps_display}", (30, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        cv2.imshow("Hand Gesture Recognition", image)

        if cv2.waitKey(5) & 0xFF == 27: 
            break

cap.release()
cv2.destroyAllWindows()
