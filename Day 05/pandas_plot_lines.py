import pandas as pd
import matplotlib.pyplot as plt

# Import our data file
stock_prices = pd.read_csv('/data/intel_amd_stock_prices.csv')

# Print DataFrame
# print(stock_prices)

# Create y-columns
y_columns = ['intel', 'amd']

# Name / assign axis
stock_prices.plot(x='month', y=y_columns)

# Create plot title
plt.title('Monthly Stock Prices')

# Create a title for y axis
plt.ylabel('Prices ($US)')

# Show the plot
plt.show()
