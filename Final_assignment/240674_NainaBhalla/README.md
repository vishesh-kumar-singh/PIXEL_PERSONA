# PIXEL PERSONA Final Project 
## Naina Bhalla
## 240674
The model identifies faces in an image use Haar Cascades and then classifies the faces into either male or female.
(The final model that I have submitted can only be run on a local runtime.)

## Overview
### Dataset
It uses a dataset with 900 images in the training dataset and 200 each in the testing and the validation set. Each of the sets have 50% male images and 50% female images.

Since the dataset that I had used had no labels with the images, just were in separate labelled folders, I added labels to them when I created DataFrames for the dataset.

I preprocessed the dataset images according to the model and encoded the labels using LabelEncoder

### Model Architecture
The model itself is composed of various layers including Conv2D,MaxPooling,BatchNormalization and Dropout. It also uses early stopping callbacks to prevent overfitting.

![Screenshot (142)](https://github.com/user-attachments/assets/56a52a9b-7c20-42cf-925d-96fed4a6f14f)


## Performance
The model gives 88.49% accuracy on the testing data and a loss of 0.30.

![Screenshot (144)](https://github.com/user-attachments/assets/ec3c906e-21e3-4b8a-ad55-959dfce71aee)

![Screenshot (143)](https://github.com/user-attachments/assets/05f4be9a-b7be-4aef-9d39-44a90859a323)


## Output Images

 ![sample_output_with_multiple_faces](https://github.com/user-attachments/assets/289a56f3-df0e-4d70-ae5f-df33db8a7dc5)

 ![output](https://github.com/user-attachments/assets/0edc3cb8-5c9a-46a6-96a3-c51ed1ac1dfb)
 
 ![multiple_faces_2](https://github.com/user-attachments/assets/ba0fda32-54a3-4866-b0b2-b193c0294ff3)

## Live Detetction
This part only runs on a local runtime using a jupyter notebook. It switches on the webcam and then detects the gender of the person on the live feed along with the probability of its prediction.


