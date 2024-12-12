<h1>Gender Detection Model</h1>

## About the project
### I have created a Gender Detection Model as a part of Winter Camp project "PIXEL PERSONA" that was conducted by ICG.
### This project detects gender of a person when an image is provided.
### It involves the application of deep neural network. I first trained the model on 3000 images of males and females who were of various ages and appearances. Then 20 images were passed in as input and the model predicted their gender accurately

## Libraries/Programming Language used
### Programming Language: Python
### Libraries/Modules: NumPy, OpenCV, TensorFlow, os, scikit-learn, HAAR Cascade

## Dataset
[Here](https://www.kaggle.com/datasets/yasserhessein/gender-dataset) you can find the dataset that I used in this project

## Metrics
### Training Accuracy: 99.83%
### Validation Accuracy: 90.33%
### Testing Accuracy: 92.80%

## Instructions for operating the model
### Please load the .ipynb file, Group Photos folder, gender_dataset and the API token named "kaggle" on Google Colab and store them under contents folder
### Ensure that the Group Photos folder contains a single image having name like "n.jpg" where n is a positive single digit number
### You can run the file using the Run all button under the Runtime tab.
### For running the model again, delete the folders Group Photos, Output images, gender_dataset.zip and gender_dataset using the commands (after uncommenting them) at the bottom of the program. Then, recreate the Group Photos folder the group photo stored in it in the same format as described earlier. Also, upload the kaggle token and then click the Run all button under Runtime tab.

## Directory Structure
### 1. gender_dataset: Contains the data imported from [Kaggle](https://www.kaggle.com/datasets/yasserhessein/gender-dataset) along with some preprocessed images in subfolders
### 2. Group Photos: Contains the pre-processed group photograph used in the program
### 3. Output images: Contains some single and 1 group photograph after it has been processed by the model.
### 4. gender_dataset.zip: Zipped form of the data downloaded from Kaggle
### 5. .ipynb file: contains code of the program

## About the Creator
### Made by Devansh Chaturvedi (Roll Nos: 240340)

## Some Sample Images:
![1](https://github.com/user-attachments/assets/30d6ca29-550c-452a-aeef-c172c838e49d)![4](https://github.com/user-attachments/assets/746e7836-ae94-4ad3-bfbd-03cc67820ddb)
![3](https://github.com/user-attachments/assets/f8bab043-da9c-4df1-821e-a2fdfae6fd28)
![2](https://github.com/user-attachments/assets/bdd6df3a-4f54-4bb3-bac3-dd3ba104720c)

