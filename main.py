# INF601 - Advanced Programming in Python
# Marcos German
# Mini Project 2
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load Netflix titles dataset
df = pd.read_csv('titles.csv')

# Display info and preview dataset
print(df.info())
print(df.head())

# Count number of movies released per year
data = df['release_year'].value_counts().sort_index()

#Create bar chart
plt.figure(figsize=(10, 6))
data.plot(kind='bar')
plt.title('Number of Netflix Movies Released per Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')

# Check if charts folder exist if not create a charts folder
charts_dir = 'charts'
if not os.path.exists(charts_dir):
    os.makedirs(charts_dir)

# Save PNG file in charts folder
charts_path = os.path.join(charts_dir, 'netflix_titles_releases_per_year.png')
plt.savefig(charts_path)

# Show plot
plt.show()