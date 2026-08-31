# Sign-language-translator
# 🤟 Real-Time Sign Language Translator

A real-time **Sign Language Recognition System** that uses computer vision and machine learning to recognize hand gestures from a webcam and convert them into corresponding alphabet characters.

The project combines **OpenCV**, **MediaPipe**, **Python**, and a **Random Forest Classifier** to detect hand landmarks and classify sign language gestures in real time.

---

## 🚀 Features

* 🎥 Real-time hand gesture detection using a webcam
* ✋ Hand landmark extraction using MediaPipe
* 🧠 Machine learning-based gesture classification
* 🔤 Recognition of sign language alphabet gestures
* ⚡ Real-time prediction using OpenCV
* 🌐 Flask-based backend for the web interface
* 📊 Custom dataset for training the classification model
* 📈 High classification accuracy on the collected dataset

---

## 🏗️ Project Architecture

```text
                    ┌─────────────────┐
                    │     Webcam      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     OpenCV      │
                    │ Frame Capture   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    MediaPipe    │
                    │  Hand Detection │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Hand Landmarks  │
                    │ 21 × (x,y,z)    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Random Forest   │
                    │   Classifier    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Predicted Sign  │
                    │   / Character   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Flask / UI    │
                    └─────────────────┘
```

---

## 🧠 How It Works

The system follows a simple computer vision and machine learning pipeline.

### 1. Capture Video

The webcam continuously captures frames using OpenCV.

### 2. Detect the Hand

MediaPipe Hands detects the user's hand and identifies **21 hand landmarks**.

Each landmark contains:

```text
x-coordinate
y-coordinate
z-coordinate
```

These coordinates are converted into numerical features that can be used by the machine learning model.

### 3. Feature Extraction

The hand landmarks are flattened into a feature vector.

For example:

```text
[x1, y1, z1, x2, y2, z2, ...]
```

This feature vector represents the position of the hand and fingers.

### 4. Machine Learning Classification

The extracted features are passed to a **Random Forest Classifier**.

The trained model predicts the corresponding sign language character.

### 5. Display Prediction

The predicted character is displayed on the live webcam feed.

---

## 🤖 Machine Learning Model

The project uses:

**Random Forest Classifier**

Configuration used during training:

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

The dataset was divided into training and testing sets using a stratified split.

```text
Training Samples: 1043
Testing Samples: 261

Test Accuracy: ~98.47%
```

> Accuracy depends on the dataset, lighting conditions, hand positioning, camera quality, and gestures used during testing.

---

## 📊 Dataset

A custom dataset was created using hand landmark coordinates extracted from MediaPipe.

Each sample contains:

* Hand landmark coordinates
* Corresponding gesture label

Example structure:

```text
x1, y1, z1, x2, y2, z2, ..., label
```

The dataset is stored as:

```text
dataset.csv
```

The project was initially developed and tested using alphabet gesture classes such as:

```text
A
B
C
```

The system can be extended by collecting additional gesture samples.

---

## 🛠️ Tech Stack

| Technology          | Purpose                                |
| ------------------- | -------------------------------------- |
| Python              | Core programming language              |
| OpenCV              | Webcam access and image processing     |
| MediaPipe           | Hand detection and landmark extraction |
| NumPy               | Numerical operations                   |
| Pandas              | Dataset processing                     |
| Scikit-learn        | Machine learning                       |
| Joblib              | Model serialization                    |
| Flask               | Backend / web interface                |
| HTML/CSS/JavaScript | Frontend                               |

---

## 📁 Project Structure

```text
Sign-Language-Translator/
│
├── dataset/
│   └── dataset.csv
│
├── model/
│   └── sign_language_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── collect_data.py
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
```

> File names may vary depending on the final version of the project.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Sign-Language-Translator
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate it:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

The main dependencies are:

```text
opencv-python
mediapipe
numpy
pandas
scikit-learn
joblib
flask
```

You can install them using:

```bash
pip install opencv-python mediapipe numpy pandas scikit-learn joblib flask
```

---

## 🧪 Training the Model

If you want to train the model using your own dataset:

```bash
python train_model.py
```

The training process:

1. Loads `dataset.csv`
2. Separates features and labels
3. Splits the dataset into training and testing sets
4. Trains the Random Forest classifier
5. Evaluates the model
6. Saves the trained model

Example output:

```text
Training samples: 1043
Testing samples: 261
Accuracy: 0.9846743295019157
```

---

## 🎥 Running the Application

Start the Flask server:

```bash
python app.py
```

The application will run locally, typically at:

```text
http://127.0.0.1:5000
```

Open the address in your browser and allow webcam access.

---

## 🔄 Real-Time Recognition Pipeline

```text
Webcam
   ↓
OpenCV Frame
   ↓
MediaPipe Hand Detection
   ↓
21 Hand Landmarks
   ↓
Feature Vector
   ↓
Random Forest Model
   ↓
Predicted Character
   ↓
Display on UI
```

---

## 📈 Model Performance

The Random Forest model achieved approximately:

**98.47% test accuracy**

on the collected dataset.

However, model accuracy alone does not guarantee perfect real-world recognition. Performance can change depending on:

* Lighting
* Camera quality
* Background
* Hand orientation
* Distance from camera
* Gesture similarity
* Individual differences in signing

---

## 🔮 Future Improvements

The project can be extended into a more complete sign language communication system.

### Planned Improvements

* 🔤 Support the complete sign language alphabet
* 📝 Combine recognized characters into words and sentences
* 🔊 Text-to-Speech conversion
* 🎙️ Speech-to-Text support
* 🤝 Two-way communication between signers and non-signers
* 📱 Mobile application
* 🌐 Improved web interface
* 🧠 Better gesture classification models
* 👥 Multi-hand gesture recognition
* 🎯 Improve robustness under different lighting conditions
* 📊 Larger and more diverse datasets
* ⚡ WebSocket-based real-time communication

---

## ⚠️ Limitations

The current version is primarily a **gesture classification prototype**.

It does not yet provide complete natural-language sign language translation.

Static hand gestures are easier to recognize than dynamic signs involving:

* Movement
* Timing
* Facial expressions
* Body posture
* Multiple hand interactions

Future versions can incorporate temporal models and additional visual features to handle these cases.

---

## 🎯 Use Cases

This system can serve as a foundation for:

* Accessibility applications
* Educational tools
* Sign language learning
* Human-computer interaction
* Assistive communication systems
* Computer vision research
* Gesture-controlled interfaces

---

## 👩‍💻 Development

This project was developed as a computer vision and machine learning project exploring the use of **hand landmark detection + classical machine learning** for real-time sign language recognition.

---

## 📜 License

This project is intended for educational and research purposes.

A suitable open-source license can be added depending on the intended use of the project.

---

## ⭐ Future Vision

The ultimate goal is to evolve this prototype into an accessible communication platform that can bridge the communication gap between **sign language users and people who do not understand sign language**.

> **From hand gestures to meaningful communication. 🤟**
