# INF601 - Advanced Programming in Python
# Marcos German
# Mini Project 2
import pandas as pd
import matplotlib.pyplot as plt

#Load Netflix titles dataset
df = pd.read_csv('titles.csv')

#Display info and preview dataset
print(df.info())
print(df.head())

#Count number of movies released per year
data = df['release_year'].value_counts().sort_index()

#Create bar chart
plt.figure(figsize=(10, 6))
data.plot(kind='bar')
plt.title('Number of Netflix Movies Released per Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.show()