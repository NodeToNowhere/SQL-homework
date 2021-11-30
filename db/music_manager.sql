DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;


CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    artist_name VARCHAR(255),
    
);
CREATE TABLE almbum(
    id SERIAL PRIMARY KEY,
    album_title VARCHAR(255)
    album genre VARCHAR(255)
    user_id INT REFERENCES artists(id)
);