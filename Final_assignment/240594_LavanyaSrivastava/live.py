import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load Haar cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the pre-trained model
model = load_model('gender_classification_model.h5')  # Replace with your model's path

# Define labels
labels = ['Female', 'Male']

# Padding factor
PADDING = 0.2 

# Start video capture
cap = cv2.VideoCapture(0) 

while True:
    # Read frame from video
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Calculate padding
        x_pad = int(w * PADDING)
        y_pad = int(h * PADDING)
        x_start = max(0, x - x_pad)
        y_start = max(0, y - y_pad)
        x_end = min(frame.shape[1], x + w + x_pad)
        y_end = min(frame.shape[0], y + h + y_pad)

        # Extract padded face ROI
        face = frame[y_start:y_end, x_start:x_end]

        # Preprocess the face for the model
        face_resized = cv2.resize(face, (224, 224)) 
        face_normalized = face_resized / 255.0 
        face_expanded = np.expand_dims(face_normalized, axis=0)

        # Predict gender
        prediction = model.predict(face_expanded, verbose=0)[0][0]
        predicted_label = labels[1] if prediction > 0.5 else labels[0]
        confidence = prediction*100 if prediction > 0.5 else (1 - prediction)*100

        cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
        cv2.putText(frame, f"{predicted_label} ({confidence:.2f})", (x_start, y_start - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow('Gender Detection', frame)

    # Break the loop with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()

