#!/usr/bin/env python

# index.py
# This file creates instances of movies and build movie trailer page

import fresh_tomatoes
import movie

# Chinese movie "Lu De Shui" or Mr. Donkey
mr_donkey = movie.Movie("Mr. Donkey", 
	"https://www.youtube.com/watch?v=jXFQQbr7EVk", 
	"https://images-na.ssl-images-amazon.com/images/M/MV5BNGQ1MzcyYWItN2Q4NC00YTlmLTg3NGEtMWY0Mzk0NDFjYTNiXkEyXkFqcGdeQXVyMjExMzEyNTM@._V1_SY1000_CR0,0,666,1000_AL_.jpg")
# Chinese movie "Shi'er Gongmin" or 12 Citizens
twelve_citizens = movie.Movie("12 Citizens", 
  "https://www.youtube.com/watch?v=n8HHV4HIYYc", 
  "https://images-na.ssl-images-amazon.com/images/M/MV5BNzcyZjlkYjUtMTdjZi00NDc5LWIyMjMtMmEwMDYzMTBhOTMzXkEyXkFqcGdeQXVyMjg0MTI5NzQ@._V1_SY1000_CR0,0,750,1000_AL_.jpg")
# Chinese movie "Luomandike Xiaowangshi" or The Wasted Times
the_wasted_times = movie.Movie("The Wasted Times", 
  "https://www.youtube.com/watch?v=FsXRUO01cRo", 
  "https://images-na.ssl-images-amazon.com/images/M/MV5BZmE0ZmI2OTgtYjVkNS00ZDkxLTg1OTYtYjI3ZDYwMzgwYzY0XkEyXkFqcGdeQXVyMjExMzEyNTM@._V1_.jpg")
# Hong Kong movie Chungking Express
chungking_express = movie.Movie("Chungking Express", 
  "https://www.youtube.com/watch?v=Bjd7PFf_TFw", 
  "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5MTc3NDE2MV5BMl5BanBnXkFtZTcwMDM5MTk5MQ@@._V1_.jpg")

movies = [mr_donkey, twelve_citizens, the_wasted_times, chungking_express]

fresh_tomatoes.open_movies_page(movies)