import pandas
import pyautogui
import time
import pandas as pd
import numpy as np
from PIL import Image


class Selection:
    def __init__(self, dist=120):
        self.left = 0
        self.upper = 1
        self.right = dist - 1
        self.lower = dist
        self.dist = dist
        self.dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    def Move(self, img, nav="a2"):
        '''
        Moves the box that outlines the requested position to crop on the board
        anywhere from a1 -> h8
        '''
        if nav == "right":
            self.left = self.right
            self.right = self.left + self.dist + 1
        if nav == "left":
            self.right = self.left
            self.left = self.right - self.dist
        if nav == "down":
            self.upper = self.lower
            self.lower = self.upper + self.dist + 1
        if nav == "up":
            self.lower = self.upper
            self.upper = self.lower - self.dist
        elif len(nav) == 2:
            coefA = self.dict[nav[0]]
            coefB = int(nav[1])
            self.left = coefA * self.dist
            self.lower = coefB * self.dist
            self.right = self.left + self.dist
            self.upper = self.lower - self.dist
            '''
            if nav == "h1":
                self.lower = img.height
                self.right = img.width
                self.upper = self.lower - self.dist
                self.left = self.right - self.dist
            if nav == "a2":
                self.lower = img.height - self.dist
                self.left = 0
                self.right = self.left + self.dist
                self.upper = self.lower - self.dist
            if nav == "a8":
                self.left = 0
                self.upper = 0
                self.right = self.dist
                self.lower = self.dist
            '''
        img = img.crop(self.ToTuple())
        #imgArr = (255 * np.round(imgArr / 255, 0)).astype(np.uint8)

        #from stackoverflow
        img.show()
        r = img.convert('L')
        r = r.point(lambda x: 1 if x < 128 else 254)
        r = r.resize((round(r.size[0]*0.2), round(r.size[1]*0.2)))
        #r.show()
        imgArr = np.asarray(r)
        imgArr = imgArr.flatten()

        return imgArr

    def ToTuple(self):
        '''
        PIL Images requires a tuple input for cropping and this does the conversion
        '''
        return (self.left, self.upper, self.right, self.lower)

#to see if there are more black or white pixels than 90% of all the pixels, but its doesn't work and wasn't necessary for now
'''
def valid(arr):
    total = len(arr)
    w = 0
    b = 0
    for pix in arr:
        if(pix) == 0:
            b += 1
        if (pix) == 1:
            w += 1
    if w > 0.9*total or b > 0.9*total:
        return False
'''

def openMe(i):
    #If the renaming process has gone wrong and a file is missing, this catches the bug
    try:
        img = Image.open(f"pics/{i}.png")
    except FileNotFoundError:
        i+=1
    img = Image.open(f"pics/{i}.png")
    #Crop 1 pixel from all sides
    #Eventually this will not be hard coded
    img = img.crop((1, 1, 965, 965))
    return img, i

'''
#Collecting the screenshots:

chromePos = 142, 1312
settingPos = 1365, 185
skinPos = 1105, 510
boardPos = 1105, 555
nestSkinPos = 1105, 530
nextBoardPos = 1105, 570
savePos = 1135, 1135
firstSkinPos = 1120, 57

time.sleep(4)
print(pyautogui.position())

pyautogui.click(chromePos)
i = 10
while i > 0:
    time.sleep(0.4)
    pyautogui.click(settingPos)
    time.sleep(0.3)
    pyautogui.click(boardPos)
    pyautogui.click(nextBoardPos)
    time.sleep(0.4)
    pyautogui.click(skinPos)
    time.sleep(0.4)
    pyautogui.scroll(20)
    time.sleep(0.3)
    pyautogui.click(firstSkinPos)
    time.sleep(0.4)
    pyautogui.click(savePos)
    pyautogui.keyDown("command")
    pyautogui.keyDown("shift")
    pyautogui.press("/")
    pyautogui.keyUp("command")
    pyautogui.keyUp("shift")
    i -= 1
    j = 32
    while j > 0:
        time.sleep(0.5)
        pyautogui.click(settingPos)
        time.sleep(0.6)
        pyautogui.click(skinPos)
        time.sleep(0.1)
        pyautogui.click(nestSkinPos)
        time.sleep(0.2)
        pyautogui.click(savePos)
        time.sleep(0.3)
        pyautogui.keyDown("command")
        pyautogui.keyDown("shift")
        pyautogui.press("/")
        pyautogui.keyUp("command")
        pyautogui.keyUp("shift")
        time.sleep(0.4)
        j -= 1

#for white
king = 0
queen = 1
rook = 2
bishop = 3
knight = 4
pawn = 5
#black = values +6
allPieces = pd.DataFrame()

#Cropping and labeling the squares of the boards:

i = 0
t1 = time.time()
print()
while i < 330:
    img, i = openMe(i)
    bbox = Selection(120)
    piece = bbox.Move(img, "a8")
    piece = np.insert(piece, 0, 8, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, 10, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, 9, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, 7, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, 6, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, 9, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, 10, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, 8, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    #top row finished after 8 iterations, now only need 2 pawns
    piece = bbox.Move(img, "down")
    piece = np.insert(piece, 0, 11, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img, "left")
    piece = np.insert(piece, 0, 11, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    #Moving to a2 for a white pawn
    piece = bbox.Move(img, "a2")
    piece = np.insert(piece, 0, pawn, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    #Moving to white rook and doing the same thing
    piece = bbox.Move(img, "down")
    piece = np.insert(piece, 0, rook, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, knight, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, bishop, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, queen, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, king, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, bishop, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, knight, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img)
    piece = np.insert(piece, 0, rook, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    piece = bbox.Move(img, "up")
    piece = np.insert(piece, 0, pawn, axis=0)
    allPieces = pd.concat([allPieces, pd.DataFrame(piece).T], axis=0)
    i += 1
    if i == 0 or i % 75 == 0:
        print(f"{i}th pass done")

#: Completion time of the fit
t2 = round(time.time() - t1, 1)
print(f"done in {t2} seconds")
'''