import pandas as pd
import matplotlib.pyplot as plt

# Import our data file
life = pd.read_csv('/data/irish_life_expec.csv')

# Print DataFrame
# print(life)

# Create Scatter Plot with x axis = year and y axis = life expectancy
life.plot(kind='scatter', x='year', y='life expec')

# Add the title
plt.title('Irish Life Expectancy')

# Add the x-axis label
plt.xlabel('Age')

# Add the y-axis label
plt.ylabel('Life Expectancy')

# Show Plot
plt.show()
