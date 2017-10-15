class Movie:
        """     Class represent a movie

                Attributes:
                    title: Title of the movie
                    poster_image_url: Url to an Image of the movie
                    trailer_youtube_url: youtube like to the trailer of the movie
         """
        def __init__(self,title,poster_image_url,trailer_youtube_url):
                """ Inits Movie Instance with the minimal informations """
                self.title                  = title                 #Title of the movie
                self.poster_image_url       = poster_image_url      #Url to the image of the movie
                self.trailer_youtube_url    = trailer_youtube_url   #Url to a youtube trailer video

        


