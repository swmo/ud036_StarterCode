from classes.movie import Movie
from classes.website import Website


"""
Generate static movies to show on the website
"""
movies = []

movie_intouchables = Movie('Intouchables',
              'https://upload.wikimedia.org/wikipedia/en/9/93/'
              'The_Intouchables.jpg',
              'https://www.youtube.com/watch?v=34WIbmXkewU')
movies.append(movie_intouchables)

movie_demaintout = Movie('Demain tout commence',
              'https://img5.cdn.cinoche.com/images/'
              'f8746917134c8ebf68d72dc89fbdd146.jpg',
              'https://www.youtube.com/watch?v=OAt0mmfW8S4')
movies.append(movie_demaintout)

movie_intowild = Movie('Into the wild',
              'http://www.gstatic.com/tv/thumb/movieposters/168385/'
              'p168385_p_v8_aa.jpg',
              'https://www.youtube.com/watch?v=2LAuzT_x8Ek')
movies.append(movie_intowild)

""" Create the Website with the movies """
website = Website(movies)
website.generate_html()
website.open_website()



