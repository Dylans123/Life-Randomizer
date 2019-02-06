# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:26:40 2018

@author: Skelito Welito
"""

import json
from yelpapi import YelpAPI
from pprint import pprint
import random

api_key = 'R2zf2a3vJ1u8EHvu_IjX88ZcpZWJSci3tUsxfOGL9z4aDUz1_la8srG2W4BiqzHeyPKfFdZ9jIko6BjpwEZ_GkWgNGd4MXzr94Hugv4Zydin-H0UwMGSKCEk49UZXHYx'

yelp_api = YelpAPI(api_key)
#activity_list = ['theater', 'park', 'ice skating', 'spa', 'movie store', 'bowling', 'thrift store']
#
#search_term_food = input("What type of meal are you interested in? Sushi, lunch, dinner, breakfast, etc.: ")
#location_term = input("Where are you located (city, state): ")
#sorted_term = input("Would you like only the top rated restaraunts in your area? (Y/N): ")
#search_term_activity = random.choice(activity_list)
#event_term = input("What type of event do you want to attend?: ")
#if sorted_term == 'Y':
#    result_sorted = 'rating'
#else:
#    result_sorted = None
    
def random_activity_generator(activity_list):
    return random.choice(activity_list)

def random_place(search_term_food, location_term, result_sorted):
    response_food = yelp_api.search_query(term = search_term_food, location= location_term, sort_by = result_sorted, limit=5)
#    pprint (response)
#    response_activity = yelp_api.search_query(term = search_term_activity, location = location_term, sort_by = result_sorted, limit=5)
#    pprint(response_activity)
    possible_food = []
    for x in response_food['businesses']:
        for y in x:
            if y == 'alias':
                possible_food.append(x[y])
#    possible_activity = []
#    for x in response_activity['businesses']:
#        for y in x:
#            if y == 'alias':
#                possible_activity.append(x[y])
    return random.choice(possible_food)

#def random_event(event_term, location_term):
#    response_event = yelp_api.featured_event_query(location = location_term )
#    return pprint(response_event)

#random_place(search_term_food, location_term, result_sorted)
#random_event(event_term, location_term)