import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array

# Load the trained model
model = tf.keras.models.load_model(r'C:\Users\Lenovo\Downloads\my_trained_model1.h5')  

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale (required by Haar Cascade)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Crop the face from the frame
        face = frame[y:y + h, x:x + w]
        
        # Preprocess the face image for the CNN model (e.g., resize and normalize)
        face_resized = cv2.resize(face, (94, 94))  # Resize to the input size of your model
        face_array = img_to_array(face_resized)
        face_array = np.expand_dims(face_array, axis=0)
        face_array = face_array / 255.0  # Normalize the pixel values if your model was trained with normalized images

        # Predict gender using the CNN model
        prediction = model.predict(face_array)

        # Handle binary classification (0 for Male, 1 for Female)
        if prediction.shape[1] == 1:  # Binary classification case
            gender = "Female" if prediction[0] > 0.5 else "Male"  # 1: Female, 0: Male
        else:  # Multi-class classification (using np.argmax to find the class)
            gender_class = np.argmax(prediction[0])  # Get the index with the highest probability
            gender_labels = ["Male", "Female"]  # 0: Male, 1: Female
            gender = gender_labels[gender_class]
        
        # Display the prediction on the frame
        cv2.putText(frame, f'Gender: {gender}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the resulting frame
    cv2.imshow('Gender Detection', frame)

    # Exit loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()