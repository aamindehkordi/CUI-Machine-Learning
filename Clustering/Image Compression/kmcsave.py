
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
#   file:   kmcimage.py                                                         #
#   author:                                                        #
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

def convert_to_kmc(image, color_count):
    """ Compresses picture images using KMeans by reducing the total number of
        colors to either 256 colors or 16 colors. The input image should be a
        2D numpy array of RGB pixels arranged width x height. The output will be
        two numpy arrays: the first is a palette of RGB colors and the second
        is a 2D lookup array using the original image dimensions and referencing
        the RGB palette.

        Note: This is a lossy compression algorithm.
    """

    if not isinstance(image, np.ndarray):
        raise ValueError('Error: image must be a numpy array')
    #if color_count != 16 and color_count != 256: # DON'T WORRY, EXACT SAME CODE FOR 16 AND 256
    #    raise ValueError('Error: compression requires 16 or 256 colors, not {}'.format(color_count))

    # Reshape from 2D image of RGB pixels to 1D sequence of RGB pixels
    height, width, depth = image.shape
    image = image.reshape(width * height, depth)

    # IMPLEMENT FUNCTION (SEE IMAD'S ARTICLE OR JUPYTER NOTEBOOK FOR HINTS)
    i = 5

    #Creating the model
    model = KMeans(n_clusters= color_count, n_init=i)
    model.fit(image)

    #Getting Labels and clusters and converting them to the proper format
    labels = model.labels_
    pixels = labels.astype(np.uint8)

    clusters = model.cluster_centers_
    palette = np.round(clusters, 0).astype(np.uint8)

    # Revert back to 2D image but this time it's just a sequence of palette IDs
    pixels = pixels.reshape(height, width)
    return palette, pixels



def save_kmc_image(palette, pixels, filename):

    if not isinstance(pixels, np.ndarray):
        raise ValueError('Error: pixels must be a numpy array')
    if not isinstance(palette, np.ndarray):
        raise ValueError('Error: palette must be a numpy array')

    # IMPLEMENT FUNCTION (ASK PROF TALLMAN FOR HINTS)

    header = 'KMC4'.encode("utf8")
    height, width = pixels.shape
    height = height.to_bytes(2, 'big')
    width = width.to_bytes(2, 'big')

    image = zlib.compress(bytes(pixels))
    frame = open(filename, 'wb')
    frame.write(header)
    frame.write(height)
    frame.write(width)
    frame.write(bytes(palette))
    frame.write(image)
    frame.close()

    return None



################################################################################
#                               MAIN PROGRAM                                   #
################################################################################

if __name__ == '__main__':

    # Handle command line arguments... automatically print help message on error
    parser = argparse.ArgumentParser(description='Compress images with the KMeans Clustering format')
    parser.add_argument('filename', type=str, help='name of a valid PNG, BMP or JPEG image file')
    parser.add_argument('colorCount', type=int, help='number of desired colors on palette')
    args = parser.parse_args()
    if not os.path.exists(args.filename) or not os.path.isfile(args.filename):
        print('Error: "{}" is not a valid file'.format(args.filename))
        exit()

    # Force 16-color compression (256 colors not required for this assignment)
    src_filename = args.filename
    dst_filename = '{}.km4'.format(src_filename)
    color_count = args.colorCount
    raw_image = imread(src_filename)

    # Compress and save the image
    palette, pixels = convert_to_kmc(raw_image, color_count)
    save_kmc_image(palette, pixels, dst_filename)

    # Output the results
    original_size = os.path.getsize(src_filename)
    compressed_size = os.path.getsize(dst_filename)
    print('  Original Size: {:>11,} bytes'.format(original_size))
    print('Compressed Size: {:>11,} bytes'.format(compressed_size))

    # Demo Purposes: show the before/after images
    # Expands the pixel array from cluster IDs to RGB values
    # Each element is the result of looking up the [R, G, B] value
    height, width = pixels.shape
    pixels = pixels.reshape(width * height)
    kmc_image = palette[pixels] # crux of regenerating image and a numpy trick
    kmc_image = kmc_image.reshape(height, width, 3)
    fig, ax = plt.subplots(1, 2)
    ax[0].set_title('Original Image')
    ax[0].imshow(raw_image)
    ax[0].axis('off')
    ax[1].set_title('KMC Compressed Image')
    ax[1].imshow(kmc_image)
    ax[1].axis('off')
    plt.tight_layout()

    plt.show()

################################################################################
#                               END OF PROGRAM                                 #
################################################################################
