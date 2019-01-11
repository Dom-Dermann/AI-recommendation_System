import pandas as pd
import numpy as np

#read in data set as data frame
frame = pd.read_csv('rating_final.csv')
cuisine = pd.read_csv('chefmozcuisine.csv')

print(cuisine)