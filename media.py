import webbrowser

class Movie():
    """Class used to store information about a movie, including the title, storyline, its poster image, and a link to its trailer"""
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        """Creates an instance of the Movie class.  Sets instance variables: title,storyline,poster_image_url,and trailer_youtube_url
           using the given parameters
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    
    def view_trailer(self):
        """Opens a new window in the web browser at the location determined by the trailer_youtube_url instance variable"""
        webbrowser.open(self.trailer_youtube_url)
