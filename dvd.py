class DVD:
    def __init__(self, movie_name, stars, producer, director, company, copies):
        self.movie_name = movie_name
        self.stars = stars
        self.producer = producer
        self.director = director
        self.company = company
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
