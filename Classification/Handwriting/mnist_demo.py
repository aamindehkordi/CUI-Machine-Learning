import pandas as pd
import numpy as np
import matplotlib.cm as cmap
import matplotlib.pyplot as plt
from PIL import Image

if __name__ == '__main__':

    print("\nMNIST")

    # Load some data from the MNIST database
    df = pd.read_csv('mnist_train.csv', nrows=20000)
    y = pd.DataFrame(df.iloc[:,-1])
    X = df.iloc[:,:-1].astype(np.uint8)
    print(X)

    # Get a sigle digit from MNIST
    some_digit = X.iloc[-1,:]
    print(f"Original Size: {some_digit.shape}")
    print(f"\n{some_digit}\n")

    # Convert from a Pandas DataFrame to a 1-D Numpy Array
    some_digit = some_digit.to_numpy()
    print(f"NP Array Size: {some_digit.shape}")
    print(f"\n{some_digit}\n")

    # We need a 2-D array to display this image
    some_digit = some_digit.reshape(28, 28)
    print(f"Resized Size:  {some_digit.shape}")
    print(f"\n{some_digit}\n")
    plt.imshow(some_digit, cmap=cmap.gray)
    plt.axis("off")
    plt.show()

    # Convert to Pillow image and save
    pimage = Image.fromarray(some_digit)
    pimage.show()
    pimage.save('mnist_digit.jpg')

    print("Done with MNIST\n")
