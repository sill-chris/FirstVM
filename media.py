

import fresh_tomatoes
import webbrowser

class Movie:

    def __init__(self, title, storyline, poster_image, trailer_youtube_url):

        self._title = title
        self._storyline = storyline
        self._poster_image_url = poster_image
        self._trailer_youtube_url = trailer_youtube_url


    def show_trailer(self):
        webbrowser.open(self._trailer_youtube_url)


def main():
     """
     Test Function
     """
     movies = []
     star_wars = Movie("Star Wars", "Star Wars",
                       "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Star_Wars_Logo.svg/250px-Star_Wars_Logo.svg.png",
                       "https://www.youtube.com/watch?v=Q0CbN8sfihY")

     toy_story = Movie("Toy Story", "Toy Story", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Toy_Story_logo.svg/300px-Toy_Story_logo.svg.png",
                       "https://youtu.be/c3986gGp3Qs")

     movies.append(star_wars)
     movies.append(toy_story)

     fresh_tomatoes.open_movies_page(movies)



if __name__ == '__main__':
     main()
     exit(0)