import pandas as pd
import matplotlib.pyplot as plt

# Import our data file
stock_prices = pd.read_csv('/data/intel_stock_price.csv')


# Print DataFrame to check
print(stock_prices)

# Plot a Bar Plot
stock_prices.plot(y='price', kind='bar')

# Name the x-axis
plt.xlabel('Month')

# Show the plot
plt.show()
