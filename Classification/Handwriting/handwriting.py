################################################################################
# This program may take some time to run on your computer depending on specs.  #
# Recommended Specs: M1 Max 32G Ram                                            #
# Minimum Specs: Intel Xeon Core 2                                             #
# Takes a user drawn input of (hopefully) a number between 0-9 and the machine,#
# after rigorous training in a non-euclidean forest, attempts to predict       #
# what number the user poorly drew on the small draw window. At the top there  #
# is a real percentage calculated by the machine during said rigorous training #
# on a test set of handwritten inputs it had never seen before. Jokes aside    #
# not too difficult, although it was a joint effort with me Kito Robby and     #
# Kyle pitching in occasionally. At first, we were running the model           #
# every single time the user pressed the button which took a long time each    #
# time, though after putting the model in 'main' much less time was taken each #
# time. Also allowed us to get the accuracy without the user having to press   #
# the button, which is why it takes so long on launch.                         #
#                                                                              #
#   A lot of the main code was from the demo files                             #
#                                                                              #
#   file:   handwriting.py                                                     #
#   author: Ali AD  & Robby LT                                                 #
################################################################################


################################################################################
import tkinter as tk
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from skimage import transform
################################################################################


################################################################################
#                         INITIALIZE DRAWING CONSTANTS                         #
################################################################################

# The user will be drawing on canvas but we can't just dump the pixels.
# Instead, we must either use platform-dependent code to take a screenshot or
# come up with some alternative. Our alternative is that we will generate an
# internal 2D array of pixels at the same time as we are drawing them.
black_pixel = np.full((1, 3), 0, dtype=np.uint8)
white_pixel = np.full((1, 3), 255, dtype=np.uint8)
test_sample = np.full((140, 140, 3), black_pixel, dtype=np.uint8)


################################################################################
#                           BUTTON HANDLERS FOR GUI                            #
################################################################################

def clear_drawing():
    '''
    Clears the drawing canvas and internal array.
    '''

    cvsCanvas.delete('all')  # drawing canvas
    predictLbl.config(text="")
    test_sample[:] = black_pixel  # internal representation of drawing


def draw_handwriting(event):
    '''
    Draws on the canvas and internal array based on mouse coordinates.
    '''

    # xy-coordinates and radius of the circle being drawn
    x = event.x
    y = event.y
    r = 2
    cvsCanvas.create_oval(x - r, y - r, x + r + 1, y + r + 1, fill='black')
    test_sample[y - 2:y + 3, x - 2:x + 3] = white_pixel


def classify_number():
    '''
    Runs Format Number and predicts using the already existing model
    '''
    test_num = format_number()
    prediction = forest.predict(test_num)
    predictLbl.config(text=f"Result: {prediction}", background='red')


################################################################################
#                                 Helper Funcs                                 #
################################################################################

def format_number():
    '''
    Robby lead a lot of this but takes the user input in the draw window and
    outputs a dataframe for the model to predict on
    '''
    #transforms the user input to the same size as training data
    size_sample = transform.resize(test_sample, output_shape=(28, 28))
    for sap in size_sample:
        for i in range(len(sap)):
            sap[i] = sap[i] * 255

    #cast the samples as an int array
    size_sample = size_sample.astype(int)
    userInput = []
    for sap in size_sample:
        for i in sap:
            userInput.append(i)

    #adding feature labels to match training data because the model gave us a warning
    columnNames = []
    for sap in range(784):
        columnNames.append("pixel" + str(sap))

    #Framing the user data
    df = pd.DataFrame(userInput)
    cols = [1, 2]
    df = df.drop(df.columns[cols], axis=1)
    df = df.swapaxes("index", "columns")
    df.columns = columnNames
    return df


def getAccuracy():
    '''
    Uses the pre-established RFC model to get an accuracy score based off of the test data which was also previously split.
    '''
    accPreds = forest.predict(X_test)
    acc = accuracy_score(y_test, accPreds)
    acc = round(acc * 100)
    return acc

################################################################################
#                                    Main                                      #
################################################################################

# Create a GUI window with a certain size and title
window = tk.Tk()
window.geometry("350x450")
window.wm_title('Handwriting Project')

# Creating the RFC model globally so program runs faster and more efficient and also to get accuracy without needing to press the button
df = pd.read_csv('mnist_train.csv')
y = df['label']
X = df.drop('label', axis='columns')
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=6, test_size=0.169, stratify=y)
forest = RandomForestClassifier(n_estimators=26, criterion='entropy', random_state=1)
forest.fit(X_train, y_train)
acc = getAccuracy()


################################################################################
#                                 DRAW THE GUI                                 #
################################################################################

# Create all the buttons and stuff. Each column will be as wide as it's widest widget. So we make some artifically wide widgets.
titleLabl = tk.Label(text=f'Handwritten Digit Classifier')
predictLbl = tk.Label(text=f'')

# This drawing canvas will be very important for our ML model
accLib = tk.Label(text=f"Random Forest Accuracy = {acc}%")
cvsCanvas = tk.Canvas(width=140, height=140, bg='white', cursor='tcross',
                      highlightthickness=1, highlightbackground='steelblue')

# The Classify button
predBttn = tk.Button(window, text='Classify Number', command=classify_number)
clsBttn = tk.Button(window, text='Reset Everything', command=clear_drawing)

# The grid layout makes sense but is a bit tedious
titleLabl.grid(row=0, column=0, columnspan=5, pady=5, padx=25)

accLib.grid(row=2, column=2, pady=5)
cvsCanvas.grid(row=3, column=2, pady=5)
predBttn.grid(row=4, column=2, pady=5)
predictLbl.grid(row=5, column=2, pady=5)
clsBttn.grid(row=6, column=2, pady=5)

cvsCanvas.bind('<B1-Motion>', draw_handwriting)
cvsCanvas.bind('<Button-1>', draw_handwriting)

default_background_color = titleLabl.cget('background')

window.resizable(False, False)
window.mainloop()

