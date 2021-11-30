import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all_albums()
artist_repository.delete_all_artists()

artist1 = Artist("Freddie")
artist_repository.save_artist(artist1)
artist2 = Artist("Michael")
artist_repository.save_artist(artist1)

album1 = Album("Good Tune", "Funk", artist1)
album_repository.save_album(album1)
album2 = Album("Hit Tune", "Pop", artist2)
album_repository.save_album(album2)

# --multiple artists??

pdb.set_trace()
