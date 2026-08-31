import cv2
import mediapipe as mp

print("Starting...")

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        print("Camera not working")
        break

    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hand
    results = hands.process(rgb)

    # Draw landmarks
    if results.multi_hand_landmarks:

        for hand in results.multi_hand_landmarks:

            for landmark in hand.landmark:
                print(landmark.x, landmark.y, landmark.z)

            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("Sign Language Translator", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()