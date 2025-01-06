class Song:
    # Class-level attributes to track the total count of songs, genres, and artists
    count = 0
    genre_count = {}
    artist_count = {}

    # Class-level lists for genres and artists
    genres = []
    artists = []

    def __init__(self, name, artist, genre):
        # Instance-level attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the total song count
        Song.count += 1

        # Add to genre_count and update genres list
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
            Song.genres.append(genre)  # Add genre to the list

        # Add to artist_count and update artists list
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
            Song.artists.append(artist)  # Add artist to the list
