import pandas as pd
import matplotlib.pyplot as plt

# Import our data file
stock_prices = pd.read_csv('/data/tesla.csv')


# Print stock_prices DataFrame for review
# print(stock_prices)

# Print using the .describe() method
# print(stock_prices.describe())

# Print the minimum value of Open
# print(stock_prices['Open'].min())

# Print the maximum value of Open
# print(stock_prices['Open'].max())

# Print the average or the mean value of Open
# print(stock_prices['Open'].mean())

stock_prices['Open'].plot(kind='box')
plt.show()
