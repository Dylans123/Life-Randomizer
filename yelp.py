# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:59:16 2019

@author: Skelito Welito
"""

from yelpapi import YelpAPI
import random

api_key = 'R2zf2a3vJ1u8EHvu_IjX88ZcpZWJSci3tUsxfOGL9z4aDUz1_la8srG2W4BiqzHeyPKfFdZ9jIko6BjpwEZ_GkWgNGd4MXzr94Hugv4Zydin-H0UwMGSKCEk49UZXHYx'

yelp_api = YelpAPI(api_key)

def random_place(search_term_food, location_term, result_sorted):
    response_food = yelp_api.search_query(term = search_term_food, location= location_term, sort_by = result_sorted, limit=5)
    possible_food = []
    for x in response_food['businesses']:
        for y in x:
            if y == 'alias':
                possible_food.append(x[y])
    choice = random.choice(possible_food)
    business = yelp_api.business_query(id = choice)
    return business

def name(business):
    name = business['name']
    return name

def location(business):
    location = ",".join(business['location']['display_address'])
    return location

def photo(business):
    try:
        photo = business['photos'][0]
        return photo
    except:
        return "No pictures available"
    
def link(business):
    url = business["url"]
    return url
    

def rating(business):
    rating = business['rating']
    return rating

#print(random_place('sushi', '(weston, florida)', 'rating'))
