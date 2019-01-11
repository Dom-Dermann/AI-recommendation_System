import pandas as pd
import numpy as np

#read in data set as data frame
frame = pd.read_csv('rating_final.csv')
# print(frame.head())
#   userID  placeID  rating  food_rating  service_rating
#   0  U1077   135085       2            2               2
#   1  U1077   135038       2            2               1
#   2  U1077   132825       2            2               2
#   3  U1077   135060       1            2               2
#   4  U1068   135104       1            1               2

cuisine = pd.read_csv('chefmozcuisine.csv')

# group the same placeIDs together by adding the amount of ratings given per place - unsorted
rating_count = pd.DataFrame(frame.groupby('placeID')['rating'].count())
# print(rating_count.head())
#           rating
#   placeID
#   132560        4
#   132561        4
#   132564        4
#   132572       15
#   132583        4

# sort the rating count by descending order to find out the highest rates place
rating_count = rating_count.sort_values('rating', ascending=False).head()
# print(rating_count.head())
#         rating
#   placeID
#   135085       36
#   132825       32
#   135032       28
#   135052       25
#   132834       25

# put the place IDs from the last step in a new data frame, 0-indexed and with column name 'placeID'
most_rated_places = pd.DataFrame([135085, 132825, 135032, 135052, 132834], index=np.arange(5), columns=['placeID'])
# print(most_rated_places.head())
#   placeID
#   0   135085
#   1   132825
#   2   135032
#   3   135052
#   4   132834

# merging the two data frames together on the common column placeID
summary = pd.merge(most_rated_places, cuisine, on='placeID')
# print(summary)
#   placeID         Rcuisine
#   0   135085        Fast_Food
#   1   132825          Mexican
#   2   135032        Cafeteria
#   3   135032     Contemporary
#   4   135052              Bar
#   5   135052  Bar_Pub_Brewery
#   6   132834          Mexican

# find out the highest frequency count of cusines in the top five locations from last step. Sort it and take the top value as the most frequent cuisine. 
highest_freq = pd.DataFrame(summary.groupby('Rcuisine').count())
highest_freq = highest_freq.sort_values('placeID', ascending=False)
highest_freq = highest_freq.reset_index()
highest_freq = highest_freq.loc[0, "Rcuisine"]


cuisine_description = cuisine['Rcuisine'].describe()
# print(cuisine_description)
# count         916
# unique         59
# top       Mexican
# freq          239
# Name: Rcuisine, dtype: object

# print the recommendation
print('You would probalb like to eat here: ' + highest_freq)
