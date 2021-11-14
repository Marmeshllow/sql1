create table if not exists Genres(
	id serial primary key,
	title varchar(40) not null unique
);


create table if not exists Collections(
	id serial primary key,
	title varchar(100) not null,
	release_date integer,
	description text
);


create table if not exists Artists(
	id serial primary key,
	artist_name varchar(50) not null
);


create table if not exists Albums(
	id serial primary key,
	title varchar(100) not null,
	release_date integer,
	description text
);


create table if not exists ArtistsAlbums(
	artist_id integer references artists(id),
	album_id integer references albums(id),
	constraint ArtistsAlbumspk primary key (artist_id, album_id)
);


create table if not exists ArtistsGenres(
	artist_id integer references artists(id),
	genres_id integer references genres(id),
	constraint ArtistsGenrespk primary key (artist_id, genres_id)
);


create table if not exists Tracks(
	id serial primary key,
	title varchar(40) not null,
	duration numeric check(duration>0),
	track_text text,
	id_album integer references albums(id)
);


create table if not exists CollectionsTracks(
	Collection_id integer references Collections(id),
	Track_id integer references Tracks(id),
	constraint CollectionsTrackspk primary key (Collection_id, Track_id)
);
