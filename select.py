import psycopg2
import sqlalchemy
import user_config

engine = sqlalchemy.create_engine(f'postgresql://{user_config.user}:{user_config.password}@localhost:5432/test')
connection = engine.connect()

out = connection.execute("""
    SELECT title, release_date FROM albums
    WHERE release_date = 2018;
""").fetchall()
print(out)
print("_" * 20)

out = connection.execute("""
    SELECT title, duration FROM tracks
    ORDER BY duration desc
    LIMIT 1;
""").fetchone()
print(out)
print("_" * 20)

out = connection.execute("""
    SELECT title FROM tracks
    WHERE duration > 210;
""").fetchall()
print(out)
print("_" * 20)

out = connection.execute("""
    SELECT title FROM collections
    WHERE release_date BETWEEN 2018 AND 2020;
""").fetchall()
print(out)
print("_" * 20)

out = connection.execute("""
    SELECT artist_name FROM artists
    WHERE artist_name NOT LIKE '%% %%';
""").fetchall()
print(out)
print("_" * 20)

out = connection.execute("""
    SELECT title FROM tracks
    WHERE title LIKE '%%my%%'
    or title LIKE '%%My%%' 
    or title LIKE '%%мой%%' 
    or title LIKE '%%Мой%%';
""").fetchall()
print(out)
print("_" * 20)
