import sqlalchemy
import data
import user_config

engine = sqlalchemy.create_engine(f'postgresql://{user_config.user}:{user_config.password}@localhost:5432/test')
connection = engine.connect()

for count, el in enumerate(data.genres):
    connection.execute(f"""
        INSERT INTO genres
        VALUES({count}, '{el}');
    """)

for count, el in enumerate(data.artists):
    connection.execute(f"""
        INSERT INTO artists
        VALUES({count},  '{el}');
    """)

for artist, genres in data.artists_genres:
    connection.execute(f"""
        INSERT INTO artistsgenres
        VALUES({artist}, {genres});
    """)

for count, el in enumerate(data.albums):
    connection.execute(f"""
        INSERT INTO albums
        VALUES({count}, '{el[0]}', {el[1]}, '{el[2]}');
    """)

for artist, album in data.artists_albums:
    connection.execute(f"""
        INSERT INTO artistsalbums
        VALUES({artist}, {album});
    """)

for el in data.tracks:
    connection.execute(f"""
        INSERT INTO tracks
        VALUES({el[0]}, '{el[1]}', {el[2]}, '{el[3]}', {el[4]});
    """)

for count, el in enumerate(data.collections):
    connection.execute(f"""
        INSERT INTO collections
        VALUES({count}, '{el[0]}', {el[1]}, '{el[2]}');
    """)

for collection, track in data.collections_track:
    connection.execute(f"""
        INSERT INTO collectionstracks
        VALUES({collection}, {track});
    """)
