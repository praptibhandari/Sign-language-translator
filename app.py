from flask import Flask, render_template, request, jsonify
import cv2
import mediapipe as mp
import numpy as np
import joblib
import base64

app = Flask(__name__)

# Load ML model
model = joblib.load("sign_model.pkl")

# MediaPipe
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json["image"]

    # Remove "data:image/jpeg;base64,"
    data = data.split(",")[1]

    # Decode image
    image_bytes = base64.b64decode(data)

    # Convert to numpy
    image_array = np.frombuffer(image_bytes, np.uint8)

    # Convert to OpenCV image
    frame = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Convert BGR → RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hand
    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]

        features = []

        for landmark in hand.landmark:

            features.extend([
                landmark.x,
                landmark.y,
                landmark.z
            ])

        # Predict
        prediction = model.predict([features])

        return jsonify({
            "prediction": prediction[0]
        })

    return jsonify({
        "prediction": "No hand"
    })


if __name__ == "__main__":
    app.run(debug=True)