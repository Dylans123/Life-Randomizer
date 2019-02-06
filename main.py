# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:26:11 2019

@author: Skelito Welito
"""

from flask import Flask, render_template, request, sessions, redirect, url_for, flash
import yelp
app = Flask(__name__)
Dylan = True

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/", methods = ["GET", "POST"])
def food():
    if request.method == "POST":
        term = str(request.form["term"])
        state = str(request.form["state"])
        city = str(request.form["city"])
        location = str((state, city))
        rating = 'rating'
        business = yelp.random_place(term,location,rating)
        name = yelp.name(business)
        location = yelp.location(business)
        rating = yelp.rating(business)
        photo = yelp.photo(business)
        link = yelp.link(business)
        return render_template(
        'foodreturn.html').format(name=name,location=location,rating=rating, photo=photo, link=link)
    return render_template("food.html")

if __name__ == "__main__":
    app.run(debug=True)