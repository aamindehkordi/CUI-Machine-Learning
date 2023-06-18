# README for the 'Regression' Directory

The 'Regression' directory in the 'CUI-Machine-Learning' repository contains several Python scripts related to regression analysis. The scripts implement various regression algorithms and use them to make predictions on housing data. The directory also contains several Jupyter notebooks and CSV files related to the housing data.

## Python Scripts

1. **2022_Spring_AliAmin_LinReg.py:** This script implements the Linear Regression algorithm. It includes a class named `LinearRegression` with methods for fitting the model, making predictions, and retrieving the coefficients and intercept of the regression line. The script loads housing data from CSV files, encodes categorical variables, splits the data into training and test sets, fits the Linear Regression model, and makes predictions.

2. **Housing Predictions.py:** This script uses a Linear Regression model to make predictions on housing prices. It loads housing data from CSV files, encodes categorical variables, splits the data into training and test sets, fits the model, and makes predictions. The predictions are then saved to a new CSV file.

3. **mylittlepony.py:** This script reads a text file named 'mlp.txt' and uses regular expressions to find all matches of a certain pattern in the text. The pattern it looks for is a sequence of uppercase letters followed by any number of lowercase letters and spaces, ending with a colon. The script then prints the unique matches it finds.

4. **python_object_example.py:** This script is an example of object-oriented programming in Python. It defines a class named `Point` with methods for calculating the distance and bearing to another point. The `Point` class is then used in the main section of the script to create two points, 'House' and 'Treasure', and calculate the distance and bearing from 'House' to 'Treasure'.

5. **webscrape.py:** This web scraping script extracts information from a specified URL. It uses the `urllib` and `BeautifulSoup` libraries to fetch and parse the webpage content. It then uses regular expressions to find matches for specific patterns in the content. The script is designed to extract names, phone numbers, and email addresses, although the email addresses are replaced with the string 'Encrypted' for privacy reasons. The script also includes a function named `employee_Scraper` that is specifically designed to scrape employee information from a webpage.
