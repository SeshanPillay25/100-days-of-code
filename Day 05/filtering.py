import pandas as pd
import matplotlib.pyplot as plt

# Read in the data file
stock_data = pd.read_csv('/data/tesla.csv')


# Print out the DataFrame to make sure it's working
# print(play_data)

# Print out all rows with reviews greater than or equal to 5
# print(play_data[play_data['Rating'] >= 5 ])

# Create a conditional filter to find 'Arcade' with the 'Genres' column
# arcade_data = play_data[play_data['Genres'] == 'Arcade']

# Print the new arcade data
# print(arcade_data)

# print(stock_data['Open'])
# print(stock_data['Open'])


# print(stock_prices[stock_prices['Open'] == 315])
print(stock_data[stock_data['Open'] == 315])
