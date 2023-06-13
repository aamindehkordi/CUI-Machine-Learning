import numpy as np
from skimage import io
from skimage import transform
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# References:
#   Scikit-Image - Basic Image Processing Operations
#     https://coderzcolumn.com/tutorials/python/scikit-image-basic-image-processing-operations

if __name__ == '__main__':

    print("\nSKLearn")

    # Open and display an image with sklearn-image
    # Notice that we're tied to matplotlib and our program blocks until the window closes
    #fig = plt.Figure(figsize=(6,6))
    skimage = io.imread('lydia.bmp')
    io.imshow(skimage)
    print(f"Original Size:  {skimage.shape}")
    print(f"\n{skimage}\n") # Notice that we have arrays of RGB pixels
    plt.axis('off')
    plt.show()


    # There's only one resize method in sklearn
    skimage = io.imread('lydia.bmp')
    skimage = transform.resize(skimage, output_shape=(200, 400))
    print(f"Resized Size:   {skimage.shape}")
    print(f"\n{skimage}\n") # RGB values transformed to 0->1 floating point
    io.imshow(skimage)
    plt.axis('off')
    plt.show()

    # Crop with slice notation
    # box = (250, 50, 575, 400)
    skimage = io.imread('lydia.bmp')
    skimage = skimage[25:375, 175:500] # y1:y2, x1:x2
    print(f"Cropped Size:   {skimage.shape}")
    io.imshow(skimage)
    plt.axis('off')
    plt.show()

    # Convert to grayscale
    skimage = io.imread('lydia.bmp')
    skimage = rgb2gray(skimage)
    io.imshow(skimage)
    plt.axis('off')
    plt.show()
    
    # Avoid warnings about lossy formats and contrast
    skimage = skimage.astype(np.uint8)
    io.imsave('gs_lydia.bmp', skimage, check_contrast=False)

    print("Done with SKLearn\n")
