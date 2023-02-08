class DVD:
    def __init__(self, movie_name, stars, producer, director, company, copies, released_date):
        self.movie_name = movie_name
        self.stars = stars  # list of actors in the movie
        self.producer = producer
        self.director = director
        self.company = company
        self.copies = copies
        self.popularity = None
        self.released_date = released_date

    def get_movie_name(self):
        return self.movie_name

    def get_stars(self):
        return self.stars

    def get_producer(self):
        return self.producer

    def get_director(self):
        return self.director

    def get_company(self):
        return self.company

    def get_copies(self):
        return self.copies

    def get_released_date(self):
        return self.released_date

    def get_popularity(self):
        return self.popularity

    def set_released_date(self, released_date):
        self.released_date = released_date

    def set_popularity(self, popularity):
        self.popularity = popularity

    def set_movie_name(self, movie_name):
        self.movie_name = movie_name

    def set_stars(self, stars):
        self.stars = stars

    def set_producer(self, producer):
        self.producer = producer

    def set_director(self, director):
        self.director = director

    def set_company(self, company):
        self.company = company

    def set_copies(self, copies):
        self.copies = copies

    def __str__(self):
        stars = ''
        for star in self.stars:
            stars += star + '\t'
        output = f"Movie Name: {self.movie_name}\n" \
                 f"Stars: {stars}\n" \
                 f"Producer: {self.producer}\n" \
                 f"Director: {self.director}\n" \
                 f"Company: {self.company}\n" \
                 f"Copies: {self.copies}\n" \
                 f"Released Date: {self.released_date}\n" \
                 f"Popularity: {self.popularity}\n"
        return output


if __name__ == '__main__':
    dvd_1 = DVD('a', ["1", "2", "3", "4", "5"], 'asdf', 'jkl', 'qwerty', 10)
    print(dvd_1)
