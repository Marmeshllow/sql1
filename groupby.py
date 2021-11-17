import psycopg2
import sqlalchemy
import user_config

engine = sqlalchemy.create_engine(f'postgresql://{user_config.user}:{user_config.password}@localhost:5432/test')
connection = engine.connect()


out = connection.execute("""
    SELECT g.title, COUNT(a.artist_id) FROM genres as g
    JOIN artistsgenres as a ON g.id = a.genres_id
    GROUP BY g.title;
    """).fetchall()
print(out)
print("_" * 20)
out = connection.execute("""
    SELECT COUNT(tracks.id) FROM tracks
    JOIN albums ON tracks.id_album = albums.id
    WHERE albums.release_date IN (2019, 2020)
    """).fetchall()
print(out)
print("_" * 20)
out = connection.execute("""
    SELECT AVG(tracks.duration), albums.title FROM tracks
    JOIN albums ON tracks.id_album = albums.id
    GROUP BY albums.title;
    """).fetchall()
print(out)
print("_" * 20)
out = connection.execute("""
    SELECT DISTINCT ar.artist_name FROM artists as ar
    JOIN artistsalbums as aa ON aa.artist_id = ar.id
    JOIN albums as al ON al.id = aa.album_id
    WHERE ar.artist_name NOT IN (
        SELECT ar.artist_name FROM artists as ar
        JOIN artistsalbums as aa ON aa.artist_id = ar.id
        JOIN albums as al ON al.id = aa.album_id 
        WHERE release_date = 2020);
    """).fetchall()
print(out)
print("_" * 20)
out = connection.execute("""
    SELECT co.title FROM collections as co
    JOIN collectionstracks as ct ON ct.collection_id = co.id
    JOIN tracks as t ON t.id = ct.track_id
    JOIN albums as al ON al.id = t.id_album
    JOIN artistsalbums as aa ON aa.album_id = al.id
    JOIN artists as ar ON ar.id = aa.artist_id
    WHERE ar.artist_name = 'Lollia'
    """).fetchall()
print(out)
print("_" * 20)
out = connection.execute("""
    SELECT al.title, COUNT(ag.genres_id) FROM albums as al
    JOIN artistsalbums as aa ON aa.album_id = al.id
    JOIN artists as ar ON ar.id = aa.artist_id
    JOIN artistsgenres as ag ON ag.artist_id = ar.id
    GROUP BY al.title
    HAVING COUNT(ag.genres_id) > 1
    """).fetchall()
print(out)
print("_" * 20)
out = connection.execute("""
    SELECT t.title from tracks as t
    LEFT JOIN collectionstracks as ct on ct.track_id = t.id
    WHERE ct.track_id IS NULL
    """).fetchall()
print(out)
print("_" * 20)
out = connection.execute("""
    SELECT ar.artist_name FROM artists as ar
    JOIN artistsalbums as aa ON aa.artist_id = ar.id
    JOIN albums as al ON al.id = aa.album_id
    JOIN tracks as t ON t.id_album = al.id
    WHERE t.duration = (SELECT MIN(duration) FROM tracks);
    """).fetchall()
print(out)
print("_" * 20)
out = connection.execute("""
    SELECT al.title, COUNT(t.id) FROM albums as al
    JOIN tracks as t ON t.id_album = al.id
    GROUP BY al.title
    HAVING COUNT(t.id) = (
        SELECT COUNT(t.id) FROM albums as al
        JOIN tracks as t ON t.id_album = al.id
        GROUP BY al.title
        ORDER BY COUNT(t.id)
        LIMIT 1);
    """).fetchall()
print(out)
print("_" * 20)