import webbrowser


class Movie():
    """ The Movie() class is used to store two functions """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ The __init__ function is a constructor that is
        automatically called when you create a new class """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ The show_trailer() function calls the webbrowser.open command,
        and directs it to the URL stored in the trailer_youtube variable """
        webbrowser.open(self.trailer_youtube_url)
