# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Define a function to create a line plot
def create_line_plot(dataframe, country1, country2, country3, country4):
    """
    Creates a line plot showing the GDP of four countries over time.

    Parameters:
    -----------
    dataframe: DataFrame
        A pandas DataFrame containing data about the GDP of different countries over time.
    country1: str
        The name of the first country to plot.
    country2: str
        The name of the second country to plot.
    country3: str
        The name of the third country to plot.
    country4: str
        The name of the fourth country to plot.

    Returns:
    --------
    None
    """
    # Create a line plot with the GDP data for the four countries
    plt.figure(figsize=(10, 5))
    plt.plot(dataframe["Country Name"], dataframe[country1], label=country1)
    plt.plot(dataframe["Country Name"], dataframe[country2], label=country2)
    plt.plot(dataframe["Country Name"], dataframe[country3], label=country3)
    plt.plot(dataframe["Country Name"], dataframe[country4], label=country4)
    plt.title("GDP of Countries")
    plt.xlabel("Years")
    plt.ylabel("GDP (in trillions $)")
    plt.xlim(1975, 2020)
    plt.legend()
    plt.savefig("line_plot.png")
    plt.show()


# Load data from a CSV file
data = pd.read_csv("gdp.csv")

# Transpose the DataFrame to make it easier to work with
data = pd.DataFrame.transpose(data)

# Use the first row of the transposed DataFrame as the column names
headers = data.iloc[0].values.tolist()
data.columns = headers

# Select the relevant rows and columns from the DataFrame
data = data[4:]

# Create a line plot using the GDP data for the four selected countries
create_line_plot(data, "United Kingdom", "China", "India", "Japan")