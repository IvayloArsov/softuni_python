def movie_organizer(*movies):
    catalogue = dict()
    for movie, genre in movies:
        if genre not in catalogue:
            catalogue[genre] = [movie]
        elif genre in catalogue:
            catalogue[genre].append(movie)

    sorted_genres = sorted(catalogue.keys(), key=lambda x: (-len(catalogue[x]), x))

    result = []
    for genre in sorted_genres:
        movies_in_genre = sorted(catalogue[genre])
        genre_info = f"{genre} - {len(movies_in_genre)}\n"
        genre_info += "\n".join([f"* {movie}" for movie in movies_in_genre])
        result.append(genre_info)

    return "\n".join(result)

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))