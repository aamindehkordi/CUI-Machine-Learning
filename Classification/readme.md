# Classification Directory README

The `Classification` directory contains several Python scripts and Jupyter notebooks that demonstrate different classification techniques using various datasets. The directory also contains the datasets used in the scripts and notebooks. Below is a brief description of each file:

- `kplot2d.py`: This script contains two main functions, `plot_clusters` and `plot_neighbor`, which are used to plot 2-dimensional clusters and samples, respectively. The `plot_clusters` function works well with data from kmeans.py.

- `mushrom.py`: This script uses the RandomForestClassifier from the sklearn.ensemble module to classify data from a CSV file named 'mushrooms_saved.csv'. The script prepares the data, splits it into training and test sets, fits the classifier to the training data, and makes predictions on the test data. The accuracy of the predictions is calculated and printed.

- `titanic.py`: This script uses the RandomForestClassifier from the sklearn.ensemble module to classify data from two CSV files named 'train.csv' and 'test.csv'. The script prepares the data, splits it into features and target sets, fits the classifier to the training data, and makes predictions on the test data. The predictions are saved in a DataFrame and printed. The accuracy of the predictions is also calculated and printed.

- `titanic_tanner.py`: This script uses the RandomForestClassifier from the sklearn.ensemble module to classify data from two CSV files named 'titanic_dataset.csv' and 'titanic_predictions.csv'. The script prepares the data, splits it into features and target sets, fits the classifier to the training data, and makes predictions on the test data. The predictions are saved in a DataFrame and printed. The accuracy of the predictions is also calculated and printed.

- `kneighbors.py`: This script uses the KNeighborsClassifier from the sklearn.neighbors module to classify data. The script prepares the data, splits it into training and test sets, fits the classifier to the training data, and makes predictions on the test data. The accuracy of the predictions is calculated and printed.

The `Classification` directory also contains a subdirectory named 'Handwriting'.
