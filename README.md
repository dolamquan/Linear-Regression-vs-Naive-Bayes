Description:

This application uses a machine learning model based on the Gaussian Naive Bayes algorithm to predict diabetes from health measurements. It provides a graphical user interface (GUI) built with Tkinter, allowing users to input health data and receive predictions on whether the input suggests a diabetes outcome. The application also displays the accuracy of the model and a classification report based on a provided dataset.

Features:

+ Data Loading: Automatically loads data from a CSV file to train the machine learning model.
+ Model Training: Trains a Gaussian Naive Bayes model using the dataset.
+ Prediction: Allows users to input health data and receive predictions on whether the input suggests a diabetes outcome
+ GUI: Provides a simple graphical user interface for user interaction.
+ Accuracy and Classification Report: Displays the accuracy of the model and a classification report based on the provided

Usage:

After launching the application, follow these steps to use it:

1. Enter values: Input the required health measurements in the respective fields.
2. Click 'Predict': Press the 'Predict' button to get the diabetes prediction based on the input values.
3. View Results: The prediction result will be displayed below the button. Additionally, the model's accuracy and the classification report are displayed at the top of the window.

Data:
The application expects a CSV file named diabetes.csv in the same directory as the script. The dataset should have the following structure:

+ Columns corresponding to health measurements (e.g., Glucose, BloodPressure, etc.).
+ A binary 'Outcome' column where 1 indicates diabetes and 0 indicates no diabetes.

Requirements:
+ pandas
+ tkinter
+ scikit-learn