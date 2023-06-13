import tkinter as tk
from tkinter import *
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import ImageTk, Image
import macro

def getAccuracy():
    '''
    Uses the pre-established RFC model to get an accuracy score based off of the test data which was also previously split.
    '''
    accPreds = forest.predict(X_test)
    acc = accuracy_score(y_test, accPreds)
    acc = round(acc * 100)
    return acc

def predictSquare():
    '''
    Crops the portion of the board neccessary and runs the one dimensional array through the random forest model
    '''
    desiredPos = entry.get()
    dict = {0:'White King', 1:'White Queen', 2:'White Rook', 3:'White Bishop', 4:'White Knight', 5:'White Pawn', 6:'Black King', 7:'Black Queen', 8:'Black Rook', 9:'Black Bishop', 10:'Black Knight', 11:'Black Pawn'}
    box = bbox.Move(r, desiredPos)
    pred = forest.predict([box])
    predictLbl.config(text=f"Result: {dict[pred[0]]}", background='green')

# Creating the RFC model globally so program runs faster and more efficient and also to get accuracy without needing to press the button
df = pd.read_csv('All.csv')
df = df.dropna()
df = df.drop('Unnamed: 0', axis=1) # I don't know why this exists in the first place
y = df['0']
X = df.drop('0', axis='columns')
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=6, test_size=0.169, stratify=y)
forest = RandomForestClassifier(n_estimators=20, criterion='entropy', random_state=1)
forest.fit(X_train, y_train)
bbox = macro.Selection(120)
acc = getAccuracy()

################################################################################
#                                 DRAW THE GUI                                 #
################################################################################
# Create a GUI window with a certain size and title
window = tk.Tk()
window.geometry("520x720")
window.wm_title('Final Project')

#Test image choosing
clicked = StringVar()
clicked.set("test1")
drop = OptionMenu(window, clicked, "test", "test 1")

#Open the image
r, i = macro.openMe(clicked.get())
img = r.resize((round(r.size[0]*0.5), round(r.size[1]*0.5)))
testImg = ImageTk.PhotoImage(img)

# Create all the buttons and labels.
titleLabl = tk.Label(text=f'Let me guess what piece is on a square.')
predictLbl = tk.Label(text=f'')
entry = tk.Entry(window)
accLib = tk.Label(text=f"Random Forest Accuracy = {acc}%")
cvsCanvas = tk.Canvas(width=img.size[0], height=img.size[1], cursor='tcross')
predBttn = tk.Button(window, text='Pick a square, ex. \'a2\'', command=predictSquare)
cvsCanvas.create_image(0, 0, anchor=NW, image=testImg)
boardBttn = tk.Button(window, text='This does not work yet')

# Grid Creation
titleLabl.grid(row=0, column=0, columnspan=5, pady=5, padx=25)
accLib.grid(row=2, column=3, pady=5)
#drop.grid(row=3, column=3)
#boardBttn.grid(row=3, column=3)
cvsCanvas.grid(row=4, column=3, pady=5)
entry.grid(row=5, column=1, columnspan=3, pady=5)
predBttn.grid(row=6, column=3, pady=5)
predictLbl.grid(row=7, column=3, pady=5)

default_background_color = titleLabl.cget('background')

window.resizable(False, False)
window.mainloop()

