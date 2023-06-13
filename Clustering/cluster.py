
################################################################################
# KMeans Clustering                                                            #
#   Clusters multi-dimensional data by repeatedly grouping each data point to  #
#   a centroid and then recalculating the centroid for the new group. The      #
#   algorithm finishes when the centroids reach a stable position.             #
#                                                                              #
#   file:   cluster.py                                                         #
#   author: prof-tallman                                                       #
################################################################################



################################################################################
#                                   IMPORTS                                    #
################################################################################

import sys
import os.path
import pandas as pd
import kmeans
import kplot2d



################################################################################
#                                 FUNCTIONS                                    #
################################################################################

def usage(program_name):
    """ Prints the program usage statement. """

    print("Usage: python {} <csv> <k#> [[col1] [col2] ...]".format(program_name))
    print("  * Top row of the CSV file must contain column headings")
    print("  * Specify [[col1] [col2] ...] headings to use for KMeans model")
    print("  * If no columns are specified, all columns are used")
    print("  * If model is 2-dimensional, it will be plotted")
    print("Ex: python {} students.csv 5 attendance grade".format(program_name))



def clean_data(raw_data, zero_blanks=False):
    """ Converts all data to numeric types. Any fields that contain an invalid
        number will either be zeroed out (if `zero_blanks`=True) or the entire
        row will be dropped (`zero_blanks`=False). Returns a tuple of the clean
        data and the # rows that were zeroed/dropped (data, # rows).
    """

    # KMeans module only works with numeric data (int64 and float64)
    # Force data to a numeric type and 'coerce' any conversion errors to NaN;
    # then count the number of rows that contain any NaN values
    clean_data = raw_data.apply(pd.to_numeric, errors='coerce')
    row_count = clean_data.isna().any(axis=1).sum()

    # Handle the NaN by either zeroeing or dropping the affected rows
    if row_count > 0:
        if zero_blanks:
            clean_data = clean_data.fillna(0)
        else:
            clean_data = clean_data.dropna()

    return (clean_data, row_count)



def tuplify_rows(df, columns=None):
    """ Generates a list of tuples from select columns in a DataFrame. Specify
        the columns as a list ['Column1', 'Column2', 'Column3', ...] or `None`
        to use all of the columns.

        Ex:    Heading1  Heading2
            0       100        99
            1        86        99
            2        82        87
            3       100        90
            4        96        82
            ...
        becomes [(100, 99), (86, 99), (82, 87), (100, 90), (96, 82), ...]
    """

    if columns is None or columns == []:
        rows = list(zip(*[df[col] for col in df.columns]))
    else:
        rows = list(zip(*[df[col] for col in columns]))
    return rows



################################################################################
#                               MAIN PROGRAM                                   #
################################################################################

if __name__ == "__main__":

    ########################################################################
    # Command line parameters error checking:                              #
    #   1. Argument count                                                  #
    #   2. CSV filename is valid                                           #
    #   3. K# is in valid range                                            #
    ########################################################################

    script_name = sys.argv[0]
    if len(sys.argv) < 3:
        print("Error: not enough parameters")
        usage(script_name)
        exit()

    filename = sys.argv[1]
    if not os.path.exists(filename) or not os.path.isfile(filename):
        print("Error: {} is not a valid file")
        usage(script_name)
        exit()

    if not sys.argv[2].isdigit():
        print("Error: k# must be a number between 2 and 10")
        usage(script_name)
        exit()

    k = int(sys.argv[2])
    if k < 2 or k > 10:
        print("Error: k# must be a number between 2 and 10")
        usage(script_name)
        exit()

    ########################################################################
    # Load raw CSV data and verify that user-columns are valid in CSV file #
    ########################################################################

    raw_data = pd.read_csv(filename)
    print("Loaded data from '{}'".format(filename))

    columns = list(raw_data.columns)
    if len(sys.argv) > 3:
        columns = sys.argv[3:]

    if len(columns) > 0 and any(c not in raw_data.columns for c in columns):
        print("Error: valid column names are {}".format(list(raw_data.columns)))
        usage(script_name)
        exit()

    ########################################################################
    # Clean the data, convert it to proper format, and run KMeans          #
    ########################################################################

    (clean_data, nan_count) = clean_data(raw_data, zero_blanks=False)
    if nan_count > 0:
        print("Cleaned {} rows".format(nan_count))
    if clean_data.shape[0] < k:
        print("Error: {} data points is not enough for k={} clusters".format(clean_data.shape[0], k))
        exit()

    data = tuplify_rows(clean_data, columns)
    print("Tuplified data for KMeans {}".format(tuple(columns)))

    ########################################################################
    # STUDENTS MUST IMPLEMENT THE kmeans.run_kmeans_algorithm FUNCTION     #
    ########################################################################
    (centroids, clusters) = kmeans.run_kmeans_algorithm(data, k)
    ########################################################################
    # STUDENTS MUST IMPLEMENT THE kmeans.run_kmeans_algorithm FUNCTION     #
    ########################################################################

    print("K={}".format(k))
    print("Centroids: {}".format(centroids))
    print("Clusters:  {}".format(clusters))

    # Plot the clusters for 2D models
    dimension_count = len(columns)
    if dimension_count == 2:
        kplot2d.plot_clusters(centroids, clusters,
                              x_label=columns[0],
                              y_label=columns[1])

    print("Successfully clustered {} data points using KMeans and k={}".format(len(data), k))
    exit()

################################################################################
#                               END OF PROGRAM                                 #
################################################################################
