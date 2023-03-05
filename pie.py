# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define a function to create a pie chart
def create_pie_chart(labels, values):
    """
    Creates a pie chart showing the top 10 food and beverage online stores.

    Parameters:
    -----------
    labels: list
        A list of strings representing the names of the online stores.
    values: list
        A list of numerical values representing the revenue of each store.

    Returns:
    --------
    None
    """
    # Create a pie chart with the given labels and values
    plt.figure()
    plt.pie(values, labels=labels, autopct='%1.2f')
    plt.title("Top 10 Food and Beverages Online Stores")
    plt.savefig("pie_chart.png")
    plt.show()

# Load data from a CSV file
dataframe = pd.read_csv("top10food.csv")

# Select the relevant rows and columns from the DataFrame
dataframe = dataframe[4:]
dataframe.columns = ['store', 'revenue']
dataframe = dataframe[['store', 'revenue']]

# Convert the DataFrame columns to NumPy arrays
stores = np.array(dataframe['store'])
revenues = np.array([float(r.replace(',', '')) for r in dataframe['revenue']])

# Create a pie chart using the arrays of store names and revenues
create_pie_chart(stores, revenues)