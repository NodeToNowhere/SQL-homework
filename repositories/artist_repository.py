from db.run_sql import run_sql

from models.artist import Artist


# -----CREATE-----

def save(artist):
    sql = "INSERT INTO artists (artist_name) VALUES (%s) RETURNING *"
    values = [artist.artist_name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    artist.id = id
    return artist

# -----READ-----

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result["artist_name"])
    return artist


def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row["artist_name"])
        artists.append(artist)
    return artists

#-----UPDATE-----

def update(artist):
    sql = "UPDATE artists SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [artist.artist_name]
    run_sql(sql, values)
    
#-----DELETE-----

def delete_all():
    sql = "DELETE  FROM users"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)