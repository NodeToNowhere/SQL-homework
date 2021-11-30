from db.run_sql import run_sql
from models.album import Album
from repositories.artist_repository as artist_repository

# -----CREATE-----

def save(album):
    sql = "INSERT INTO albums (title, artist_id, genre) VALUES (%s,%s,%s) RETURNING *"
    values = [album.title, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id
    return album

# -----READ-----

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result["artist_id"])
        album = Album(
            result['title'],
            result['genre']
        )
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row["artist_id"])
        Album = Album(
            row["title"],
            row["genre"]
        )
        albums.append(Album)
    return albums

#-----UPDATE-----

def update(album):
    sql = "UPDATE albums SET (title, artist_id, genre) = (%s,%s,%s,%s) WHERE is = %s"
    values = [album.title, album.artist.id, album.genre, album.id]
    run_sql(sql, values)
    
#-----DELETE-----

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM album WHERE id = %s"
    values = [id]
    run_sql(sql, values)
