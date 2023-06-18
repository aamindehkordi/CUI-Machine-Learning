# Visual Chess Detection Final Project

The 'Visual Chess Detection' directory in the 'CUI-Machine-Learning' repository contains several Python scripts and a Jupyter notebook, as well as a CSV file named 'All.csv'. The Python scripts include 'final.py' and 'macro.py', and the Jupyter notebook is named 'final.ipynb'.

## Python Scripts

### final.py

This script uses a Random Forest Classifier (RFC) model to predict what piece is on a specific square of a chess board. The script uses the `tkinter` library to create a graphical user interface (GUI) where the user can input a square (e.g., 'a2') and the script will predict what piece is on that square. The script uses a CSV file named 'All.csv' as its dataset, and splits this data into training and test sets. The RFC model is trained on the training set and then used to make predictions. The script also includes a function named `getAccuracy` that calculates the accuracy of the RFC model based on the test data.

### macro.py

This script uses the `pyautogui` library to automate the process of collecting screenshots of different chess boards and pieces. The script then uses the `PIL` library to crop and resize the images, and convert them to grayscale. The script also includes a class named `Selection` that is used to move a cropping box around the chess board to capture images of individual squares. The script then flattens the image arrays and inserts them into a pandas DataFrame, along with a label indicating what piece is on the square. This DataFrame is used as the dataset for the machine learning model in the 'final.py' script.
