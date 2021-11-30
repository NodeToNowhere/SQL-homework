from db.run_sql import run_sql
from models.artist import Artist

# -----CREATE-----


def save_artist(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


# -----READ-----


def select_artist(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result["artist_name"])
    return artist


def select_all_artists():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row["artist_name"])
        artists.append(artist)
    return artists


# -----UPDATE-----


def update_artists(artist):
    sql = "UPDATE artists SET (first_name, last_name) = (%s) WHERE id = %s"
    values = [artist.artist_name]
    run_sql(sql, values)


# -----DELETE-----


def delete_all_artists():
    sql = "DELETE  FROM artists"
    run_sql(sql)


def delete_artist(id):
    sql = "DELETE  FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)
