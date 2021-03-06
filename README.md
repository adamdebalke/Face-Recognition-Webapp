# Face-Recognition-Webapp (Gender Detection)

<p align="center"><img src="https://github.com/adamdebalke/Face-Recognition-Webapp/blob/main/img.png" width="95%" height="95%"></p>  
Face Recognition Web Project using Machine Learning in Flask Python
A facial recognition system is a technology capable of identifying or 
verifying a person from a digital image or a video frame from a video source.

Face recognition is one of the most widely used in my application. 
If at all you want to develop and deploy the application on the web only 
knowledge of machine learning or deep learning is not enough. You also need
to know the creation of pipeline architecture and call it from the client-side,
HTTP request, and many more. While doing so you might face many challenges while 
developing the app. This course is structured in such a way that you can able to 
develop the face recognition based web app from scratch.

For the preprocess images, i  extract features from the images, ie. computing Eigen 
images using principal component analysis. With Eigen images, we will train the Machine 
learning model and also learn to test our model before deploying, to get the best results 
from the model we will tune with the Grid search method for the best hyperparameters.

Once our machine learning model is ready,i develop a web server gateway interphase in
flask by rendering HTML CSS and bootstrap in the frontend and in the backend written in Python.
Finally, create the project on the Face Recognition project by integrating the machine learning model to Flask App .

## Installation
    ** Install Python **
    Install and Create a virtual Enviroment
     # Install a virtual enviroment 
        For Windows 
        ```python
            pip install --user virtualenv
        ```
        #For Linux or Mac
             ```python
           python -m pip install --user virtual env
          ```
    #Create A virtual Enviroment
      #For Windows 
        ```python
            python -m venv "the name of the virtual enviroment"
        ```
      #For Linux or Mac
        ```python
            python -m venv "the name of the virtual enviroment"
        ```
    #Install The Requirements 
      ```python
            pip install -r requiremnts.txt
        ```
    #Install OpenCv 
     ```python
            pip install opencv-pytohn
        ```
## Usage
 
```python
      python main.py
    ```

**Facial Recognition** - [`Demo`](https://github.com/adamdebalke/Face-Recognition-Webapp/blob/main/Demo.mp4)