#!/usr/bin/env python

# movie.py
# This file defines the movie class in movie-trailer website.

class movie():
    # the class for storing information of movies
    # all values are strings
    def __init__(self, title, youtube_trailer, storyline, poster_image):
        # the title of the movie
        self.title = title
        # the url to the trailer on youtube
        self.youtube_trailer = youtube_trailer
        # a brief storyline
        self.storyline = storyline
        # url to a poster image, preferrably in the original language
        self.poster_image = poster_image
