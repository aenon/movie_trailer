#!/usr/bin/env python

# movie.py
# This file defines the movie class in movie-trailer website.

class Movie():
    # the class for storing information of movies
    # all values are strings
    def __init__(self, title, trailer_youtube_url, poster_image_url):
        # the title of the movie
        self.title = title
        # the url to the trailer on youtube
        self.trailer_youtube_url = trailer_youtube_url
        # url to a poster image, preferrably in the original language
        self.poster_image_url = poster_image_url
