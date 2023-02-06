class DVD:
    def __init__(self, movie_name, stars, producer, director, company, copies):
        self.movie_name = movie_name
        self.stars = stars # list of actors in the movie
        self.producer = producer
        self.director = director
        self.company = company
        self.copies = copies

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
        output = f"Movie Name: {self.movie_name}\n" \
                 f"Stars: {self.stars}\n" \
                 f"Producer: {self.producer}\n" \
                 f"Director: {self.director}\n" \
                 f"Company: {self.company}\n" \
                 f"Copies: {self.copies}\n"
        return output


if __name__ == '__main__':
    dvd_1 = DVD('a', [1, 2, 3, 4, 5], 'asdf', 'jkl', 'qwerty', 10)
    print(dvd_1)
