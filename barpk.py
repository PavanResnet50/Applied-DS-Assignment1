import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_market_cap(df, country):
    """   
    Parameters
    ----------
    df : DataFrame
        The dataframe containing the market capitalization data.
    country : str
        The name of the country to be plotted.

    Returns
    -------
    None.

    """
    plt.figure(figsize=(10,6))
    plt.bar(df['Country Name'], df[country], label=country)
    plt.xlabel("Year")
    plt.ylabel("% of GDP")
    plt.title(f"Market Capitalization of Listed Companies in {country} (% of GDP)")
    plt.xticks(np.arange(2000,2021,2.0))
    plt.xlim(2000,2020)
    plt.savefig(f"{country}_market_cap.png")
    plt.show()

# read the market capitalization data from an Excel file
df = pd.read_csv('market.csv')

# transpose the dataframe and set the column headers
df = pd.DataFrame.transpose(df)
header = df.iloc[0].values.tolist()
df.columns = header

# remove the first 4 rows of the dataframe
df = df[4:]

# plot the market capitalization data for India
plot_market_cap(df, "India")
