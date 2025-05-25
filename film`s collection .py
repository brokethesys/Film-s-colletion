class Film:
    def __init__(self, name, maker, release_year):
        self.name = name
        self.maker = maker
        self.release_year = release_year

    def __repr__(self):
        return f"Film(name='{self.name}', maker='{self.maker}', release_year={self.release_year})"


class FilmLibrary:
    def __init__(self):
        self._films = {}

    def add(self, film):
        self._films[film.name] = film

    def delete(self, name):
        if name in self._films:
            del self._films[name]
        else:
            print(f"Film '{name}' does not exist in the library.")

    def get(self, name):
        return self._films.get(name)

    def all_films(self):
        return list(self._films.values())

    def __iter__(self):
        return iter(self._films.values())


if __name__ == "__main__":
    library = FilmLibrary()

    film_a = Film("Inception", "Christopher Nolan", 2010)
    film_b = Film("The Matrix", "Lana Wachowski, Lilly Wachowski", 1999)

    library.add(film_a)
    library.add(film_b)

    print("Films currently in library:")
    for f in library:
        print(f)

    searched = library.get("Inception")
    print(f"Found film: {searched}")

    library.delete("The Matrix")
    print("Library after deletion:")
    for f in library:
        print(f)
