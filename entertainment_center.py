import fresh_tomatoes
import media

"""
declare favorite movies, with 4 args each:
title (movie's title)
year (year movie was released)
poster_url (url to poster image)
trailer_url (url to youtube trailer)
"""
groundhog_day = media.Movie(
    "Groundhog Day",
    1993,
    "http://goo.gl/Xhl8Ma",
    "https://www.youtube.com/watch?v=tSVeDx9fk60")

aliens = media.Movie(
    "Aliens",
    1986,
    "http://goo.gl/BB9U80",
    "https://www.youtube.com/watch?v=bTCaVjQ8nU4")
the_big_lebowski = media.Movie(
    "The Big Lebowski",
    1998,
    "http://goo.gl/2cxt3f",
    "https://www.youtube.com/watch?v=cd-go0oBF4Y")

time_bandits = media.Movie(
    "Time Bandits",
    1981,
    "http://goo.gl/yndMxB",
    "https://www.youtube.com/watch?v=Yd4DBq8a2y0")
pulp_fiction = media.Movie(
    "Pulp Fiction",
    1994,
    "http://goo.gl/V5fb9n",
    "https://www.youtube.com/watch?v=ewlwcEBTvcg")

fight_club = media.Movie(
    "FIGHT CLUB",
    "1999",
    "http://goo.gl/BR5nIh",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")

house_of_cards = media.Movie(
    "HOUSE OF CARDS",
    "2017",
    "https://i1.wp.com/www.heyuguys.com/images/2012/11/House-of-Cards-Poster.jpg?fit=673%2C960",
    "https://www.youtube.com/watch?v=ULwUzF1q5w4")
lost = media.Movie(
    "LOST",
    "2016",
    "https://i.pinimg.com/originals/f9/32/ba/f932babd0715f60d140873d363152523.jpg",
    "https://www.youtube.com/watch?v=_6vudAsjPrA")
limitless = media.Movie(
    "LIMITLESS",
    "2015",
    "http://playerlunla.com/upload/files/nwjjvimlwygrirmnjmng.jpg",
    "https://www.youtube.com/watch?v=SS5SPPwrcT8")
back_to_the_future = media.Movie(
    "Back to the Future",
    1985,
    "http://goo.gl/IxgBni",
    "https://www.youtube.com/watch?v=yosuvf7Unmg")
faq_about_time_travel = media.Movie(
    "FAQ About Time Travel",
    2009,
    "http://goo.gl/somUuo",
    "https://www.youtube.com/watch?v=a6SVDNQmyA4")
matrix = media.Movie(
    "The Matrix",
    1999,
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8")


# assign individual movies to movies array
movies = [the_big_lebowski,house_of_cards,limitless,fight_club,lost,faq_about_time_travel,groundhog_day,pulp_fiction,aliens,matrix,back_to_the_future,time_bandits]

# call movie trailer page method and pass movies array and sorting option
fresh_tomatoes.open_movies_page(movies)