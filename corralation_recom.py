# based on pearson's r 
# evaluates linear correlation r=1, strong linear relationship

import numpy as np
import pandas as pd

frame = pd.read_csv('rating_final.csv')
cuisine = pd.read_csv('chefmozcuisine.csv')
geodata = pd.read_csv('geoplaces2.csv', encoding="ISO-8859-1")

# create subset to limit data in frame
places = geodata[['placeID', 'name']]

rating = pd.DataFrame(frame.groupby('placeID')['rating'].mean())
rating['rating_count'] = pd.DataFrame(frame.groupby('placeID')['rating'].count())

# print(rating.describe)
sorted_rating = rating.sort_values('rating_count', ascending=False)
sorted_rating = sorted_rating.reset_index()
most_pop = sorted_rating.loc[0, 'placeID']

#create filter
most_pop_place = places[places['placeID'] == most_pop]
most_pop_place_cuisine = cuisine[cuisine['placeID'] == most_pop]

print(most_pop_place_cuisine)
print(most_pop_place)

places_crosstab = pd.pivot_table(data=frame, values='rating', index='userID', columns='placeID')
print(places_crosstab.head())

#print('The most popular place is: ' + most_pop_place + ' and they serve ' + most_pop_place_cuisine)