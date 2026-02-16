Flask App README

This is a Flask web application that uses a trained machine learning model 
to predict prices based on input features.

Prerequisites

Make sure you have the following software installed on your system:

    Python (version 3.6 or later)
    Flask
    joblib
    numpy

Installation

    Clone this repository or download the code files.

    Open a terminal or command prompt and navigate to the project directory.

    write the following commands before starting the project:
        pip install flask joblib numpy
    
Usage

    Start the Flask application by running the following command:
        python App.py
    Open a web browser and go to http://localhost:5000 to access the application.

    Use the web interface to input the required features and click the "Predict" button to see the predicted price


Project Structure

    app.py: The main Flask application file that defines the routes and handles requests.
    model.joblib: The trained machine learning model.
    index.html: The HTML template file for the home page.    
    train_and_model.py: The training and model creation file.
    Hyderabad.csv : dataset used for training.

    templates folder: Contains the HTML templates used by the application.
    static folder : Contains the styling file like css, javascript etc.
