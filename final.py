import tkinter as tk
from tkinter import messagebox
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# Load the dataset
data = pd.read_csv('diabetes.csv')

# Split the data into features and target
X = data.drop(columns=['Outcome'])
Y = data['Outcome']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train the model
model = GaussianNB()
model.fit(X_train, y_train)

# Calculate accuracy and classification report
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Function to make a prediction based on input values
def predict():
    try:
        input_data = [float(entry.get()) for entry in entries]
        prediction = model.predict([input_data])[0]
        outcome = "Diabetic" if prediction == 1 else "No Diabetes"
        result_text.set(f'Prediction: {outcome}')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create the main application window
root = tk.Tk()
root.title("Diabetes Prediction")

# Display the accuracy report at the top of the GUI
accuracy_label = tk.Label(root, text=f'Accuracy: {accuracy:.2f}', font=('Helvetica', 12))
accuracy_label.pack(pady=5)

report_label = tk.Label(root, text="Classification Report:", font=('Helvetica', 12))
report_label.pack(pady=5)

report_text = tk.Text(root, height=10, width=60)
report_text.insert(tk.END, report)
report_text.pack(pady=5)

# List of feature names
features = data.columns[:-1]

# Create a list to store entry widgets
entries = []

# Create entry fields for each feature
for feature in features:
    frame = tk.Frame(root)
    frame.pack(pady=5)
    
    label = tk.Label(frame, text=f"{feature}: ", width=20, anchor='w')
    label.pack(side='left')
    
    entry = tk.Entry(frame)
    entry.pack(side='left')
    
    entries.append(entry)

# Button to make a prediction
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.pack(pady=10)

# Label to display the prediction result
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=('Helvetica', 14))
result_label.pack(pady=10)

# Run the application
root.mainloop()
