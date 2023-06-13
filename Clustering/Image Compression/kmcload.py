
################################################################################
# KMC Image Compression                                                        #
#   Compresses BMP images using KMeans Clustering by downsampling them to      #
#   either 16 colors (high compression) or 256 (low compression) colors. The   #
#   algorithm sets the clutser count `k` to the desired number of colors and   #
#   then uses KMeans to identify the `k` most representative colors. Each      #
#   centroid holds the RBG value of one of the representative colors and the   #
#   image is nothing more than an array with each element holding the index of #
#   on of these colors from the palette.                                       #
#                                                                              #
#   file:   kmcload.py                                                         #
#   author: prof-tallman                                                       #
#                                                                              #
# Acknowledgements:                                                            #
#   Imad Dabbura - https://medium.com/towards-data-science/                    #
#                  k-means-clustering-algorithm-applications-evaluation-       #
#                  methods-and-drawbacks-aa03e644b48a                          #
################################################################################



################################################################################
#                                   IMPORTS                                    #
################################################################################

import os.path
import zlib
import argparse
import numpy as np
from sklearn.cluster import KMeans
from matplotlib.image import imread
import matplotlib.pyplot as plt



################################################################################
#                                   MODULE                                     #
################################################################################

def load_kmc_image(filename):
    """ Reads a KMeans Compressed image file from disk. The output will be two
        numpy arrays: the first is a palette of RGB colors and the second is a
        2D lookup array using the original image dimensions and referencing the
        RGB palette.
    """

    # KMC file format starts with 4 byte header, 2 byte width, 2 byte height
    # Then it has a palette that is either 3 * 16 colors or 3 * 256 colors
    # Rest of the file is a sequence of 1-byte pixels...
    #    ...but they're zlib compressed to save space
    with open(filename, 'rb') as f:
        header = f.read(4).decode('utf8')
        width = int.from_bytes(f.read(2), byteorder='big')
        height = int.from_bytes(f.read(2), byteorder='big')
        if header == 'KMC4':
            palette_size = 16
        elif header == 'KMC8':
            palette_size = 256
        else:
            raise ValueError("Corrupt KMC file: header specifies {} colors".format(palette_size))
        palette_buffer = f.read(3 * palette_size)
        pixel_buffer = f.read()

    # Convert from a sequence of bytes to numpy... remember to unzip pixels
    palette = np.frombuffer(palette_buffer, dtype=np.uint8)
    pixel_buffer = zlib.decompress(pixel_buffer)
    pixels = np.frombuffer(pixel_buffer, dtype=np.uint8)

    # Sanity checks on the size of the palette and number of pixel values
    if len(palette) != 3 * palette_size:
        raise ValueError("Corrupt KMC file: palette length of {} is incorrect {} colors".format(len(palette), 3 * palette_size))
    if len(pixels) != width * height:
        raise ValueError("Corrupt KMC file: dimensions of {} x {} are incorrect for {} pixels".format(width, height, len(pixels)))

    # Shape `palette` as an array of RGB values and `pixels` to height x width
    palette = palette.reshape(palette_size, 3)
    pixels = pixels.reshape(height, width)
    return palette, pixels



def convert_from_kmc(palette, pixels):
    """ Converts a KMeans Compressed image back to an RGB image that can be
        processed like any other BMP image file. Palette is a numpy array of
        RGB values that should be either 16 or 256 in length. Pixels is a
        numpy array of indices into the palette array. Returns an 2D numpy
        array of RGB values similar to matplotlib.image.imread().
    """

    if not isinstance(palette, np.ndarray):
        raise ValueError('Error: palette must be a numpy array')
    if not isinstance(pixels, np.ndarray):
        raise ValueError('Error: pixels must be a numpy array')

    # Get the image dimensions
    height, width = pixels.shape
    pixels = pixels.reshape(width * height)
    if len(palette) < max(pixels):
        raise ValueError('Error: palette does not have enough colors for these pixels')

    # Expands the pixel array from cluster IDs to RGB values
    # Each element is the result of looking up the [R, G, B] value
    image = palette[pixels]
    image = image.reshape(height, width, 3)
    return image



################################################################################
#                               MAIN PROGRAM                                   #
################################################################################

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Load images saved with the KMeans Clustering format')
    parser.add_argument('filename', type=str, help='name of a valid PNG, BMP or JPEG image file')
    args = parser.parse_args()

    # Read the file from disk and convert to a 1-D array of RGB pixels
    if not os.path.exists(args.filename) or not os.path.isfile(args.filename):
        print('Error: "{}" is not a valid file'.format(args.filename))
        exit()

    # Load and decompress the image
    palette, pixels = load_kmc_image(args.filename)
    image = convert_from_kmc(palette, pixels)

    # Show the color palette
    if len(palette) == 16:
        cols, rows = 8, 2
    else:
        cols, rows = 8, 8
    color_blocks = [np.full([100, 100, 3], color) for color in palette]
    fig, ax = plt.subplots(rows, cols, figsize=(cols, rows))
    for i in range(rows):
        for j in range(cols):
            ax[i][j].axis('off')
            color_index = i*cols + j
            ax[i][j].imshow(color_blocks[color_index])

    # Display the image
    plt.figure()
    plt.title('KMC Compressed Image')
    plt.imshow(image)
    plt.axis('off')
    plt.tight_layout()

    plt.show()

################################################################################
#                               END OF PROGRAM                                 #
################################################################################
