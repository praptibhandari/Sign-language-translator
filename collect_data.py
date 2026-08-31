import cv2
import mediapipe as mp
import csv
import os

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)

cap = cv2.VideoCapture(0)

# Create CSV file
file_exists = os.path.exists("dataset.csv")

with open("dataset.csv", "a", newline="") as file:

    writer = csv.writer(file)

    # Header
    if not file_exists:
        header = []

        for i in range(21):
            header.extend([f"x{i}", f"y{i}", f"z{i}"])

        header.append("label")
        writer.writerow(header)

    label = input("Enter sign label (A/B/C): ").upper()

    print(f"Collecting data for {label}...")
    print("Press Q to stop.")

    while True:

        success, frame = cap.read()

        if not success:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb)

        if results.multi_hand_landmarks:

            for hand in results.multi_hand_landmarks:

                data = []

                for landmark in hand.landmark:
                    data.extend([
                        landmark.x,
                        landmark.y,
                        landmark.z
                    ])

                data.append(label)

                writer.writerow(data)

                mp_draw.draw_landmarks(
                    frame,
                    hand,
                    mp_hands.HAND_CONNECTIONS
                )

        cv2.imshow("Collecting Data", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()