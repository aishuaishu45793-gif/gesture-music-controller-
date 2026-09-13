import cv2
from hand_tracker import HandTracker
from gesture_recognizer import GestureRecognizer
from music_controller import MusicController

def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    recognizer = GestureRecognizer()
    controller = MusicController()

    print("Gesture Music Controller started!")
    print("Show your hand to the camera:")
    print("  0 fingers = Pause")
    print("  1 finger  = Play")
    print("  2 fingers = Next track")
    print("  3 fingers = Previous track")
    print("  4 fingers = Volume down")
    print("  5 fingers = Volume up")
    print("Press Q to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # mirror the camera

        tracker.process(frame)
        landmarks = tracker.get_landmarks(frame)
        frame = tracker.draw_hands(frame)

        gesture = recognizer.recognize(landmarks)
        finger_count = recognizer.count_fingers(landmarks)

        controller.execute(gesture)

        # Display info on screen
        cv2.putText(frame, f"Gesture: {gesture}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Fingers: {finger_count}", (10, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow("Gesture Music Controller", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
