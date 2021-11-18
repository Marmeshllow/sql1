import psycopg2
import user_config
import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

engine = sq.create_engine(f'postgresql://{user_config.user}:{user_config.password}@localhost:5432/orm_test')
Session = sessionmaker(bind=engine)


class Artist(Base):
    __tablename__ = 'artist'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    albums = relationship('Album', back_populates='artist')


class Album(Base):
    __tablename__ = 'album'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    tracks = relationship('Track', backref='album', cascade='all,delete')
    published = sq.Column(sq.Date)
    id_artist = sq.Column(sq.Integer, sq.ForeignKey('artist.id'))
    artist = relationship(Artist)


class Genre(Base):
    __tablename__ = 'genre'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    tracks = relationship('Track', secondary='track_to_genre', back_populates='genres', cascade='all,delete')


class Track(Base):
    __tablename__ = 'track'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    duration = sq.Column(sq.Integer, nullable=False)
    genres = relationship(Genre, secondary='track_to_genre', back_populates='tracks', cascade='all, delete')
    id_album = sq.Column(sq.Integer, sq.ForeignKey('album.id', ondelete='CASCADE'))


track_to_genre = sq.Table(
    'track_to_genre', Base.metadata,
    sq.Column('genre_id', sq.Integer, sq.ForeignKey('genre.id')),
    sq.Column('track_id', sq.Integer, sq.ForeignKey('track.id'))
)

d = {
    'a1': [
        {'name': 't11', 'duration': 60},
        {'name': 't12', 'duration': 70},
        {'name': 't13', 'duration': 80}
    ],
    'a2': [
        {'name': 't21', 'duration': 60},
        {'name': 't22', 'duration': 70},
        {'name': 't23', 'duration': 80}
    ]
}


if __name__ == '__main__':
    session = Session()
    Base.metadata.create_all(engine)

    # a1 = Artist(name='Nyanners')
    # g1 = Genre(title='Chaos')
    # al1 = Album(title='Single', published='25.07.2020', artist=a1)
    # t1 = Track(title='SEISO', duration=236, album=al1)
    # t1.genres.append(g1)
    # list1 = [a1, g1, al1, t1]
    # session.add_all(list1)
    # session.commit()

    result = session.query(Track).filter(Track.title == 'SEISO').all()
    for row in result:
        print(row.title, row.genres[0].title)


    # result = session.query(Track).filter(Track.title == 'SEISO').all()
    # for row in result:
    #     print(f'title:{row.title}, duration:{row.duration}')


    # artist_1 = Artist(name='Artist_1')
    # for album_name, album_data in d.items():
    #     _album = Album(title=album_name, artist=artist_1)
    #     session.add(_album)
    #     tracks = []
    #     for track_data in album_data:
    #         _track = Track(title=track_data['name'], duration=track_data['duration'], album=_album)
    #         tracks.append(_track)
    #     session.add_all(tracks)
    # session.commit()
