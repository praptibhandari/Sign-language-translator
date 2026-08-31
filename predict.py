import cv2
import mediapipe as mp
import joblib

# Load trained model
model = joblib.load("sign_model.pkl")

# MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)

# Camera
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand in results.multi_hand_landmarks:

            # Get 63 features
            data = []

            for landmark in hand.landmark:
                data.extend([
                    landmark.x,
                    landmark.y,
                    landmark.z
                ])

            # Predict
            prediction = model.predict([data])

            letter = prediction[0]

            # Show prediction
            cv2.putText(
                frame,
                f"Sign: {letter}",
                (50, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                2,
                (0, 255, 0),
                3
            )

            # Draw hand
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