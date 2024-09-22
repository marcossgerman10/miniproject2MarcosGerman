# INF601 - Advanced Programming in Python
# Marcos German
# Mini Project 2
import pandas as pd

#Load Netflix titles dataset
df = pd.read_csv('titles.csv')

#Display info and preview dataset
print(df.info())
print(df.head())
