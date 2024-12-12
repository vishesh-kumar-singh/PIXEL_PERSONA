# PIXEL PERSONA: Gender Classification from Images using Convolutional Neural Networks (CNN)

## Table of Contents


---

## Project Overview
This project is a part of Winter Projects, 2024 by Institute Consulting group, IIT Kanpur. It builds a Convolutional Neural Network (CNN) to classify images of people into two categories: Female or Male. The model is built from scratch and we've not used any pre-trained models to achieve the result. The model achieved an accuracy of 95.308% on the testing data.

## Features
- Gender detection of images in test dataset and measurement of accuracy of the model!
- Gender detection using custom images that can be uploaded by the user!!
- Live Gender detection using image captured by a user from their own webcam!!!

## Dataset
The kaggle dataset used for training and testing this model can be found [here](https://www.kaggle.com/datasets/yasserhessein/gender-dataset). Since the dataset is quite large, we've taken 12,000 training and 12,000 testing examples, equally divided between both the labels i.e. male and female. Further, we've divided the training data to get 2,000 examples for validation and 10,000 examples for training.

## Contents of the folder
### model.ipynb
The folder contains an ipynb file named model.ipynb which contains the complete code. The code is well explained using the comments and text cells. Each code cell is marked using a number for reference. User can find all the details to run each feature of the model in the form of text and comments in the model itself. Within the ipynb file, you will find the results of the model on 20 test images. The model is also tested on 2 custom images, which are exclusive of those present in the kaggle dataset. User will also find the instructions to upload and test their own custom images if they would like to. Lastly, I tested the live gender detection feature on myself. The model also provides instructions on how the user can use the live gender detection feature themselves.
### Results folder
The Results folder contains the images of the results of our model on 20 images from test dataset, 2 custom images and 1 image from live gender detection.
### Live_Gender_Detection.mp4
This is a video of the live gender detection feature in action with me being the subject of gender detection.

## Summary of the model
**The numbers used here for reference are marked in each corresponding code cell.**
1. Uploading the kaggle dataset
2. Importing the required librarie and classes. (We will import more stuff as we move on with the code)
3. Loading limited data from dataset folder into numpy arrays and changing all images to 64x64 size for uniformity. Combining the loaded male and female data and shuffling it.
4. View some sample images from train dataset.
5. Dividing training data into training and validation data.
6. Applying Haar Cascade on our training and validation images, so that our model focuses on faces in the image instead of the entire image.
7. Building the CNN Model.
8. Compiling the model.
9. Training the model.
10. Saving the model.
11. Analysing loss and accuracy on test dataset.
12. Testing the model specifically on 20 randomly picked images from test dataset.
13. Creating a function to predict the gender of an image given the path of the image.
14. Code cell to upload custom images.
15. User can add the path of the uploaded image in the given path_list and run the code cell to get gender predictions for custom images.
16. Creating a function to access webcam with a button to capture image at desired instant.
17. Code cell to predict gender for the captured image.

##  Made by
**Vivek Chandwani**<br>
**Roll no. : 241183**
