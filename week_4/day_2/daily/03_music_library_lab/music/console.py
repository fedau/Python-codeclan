import pdb
from models.albums import Album
from models.artists import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist_repository.delete_all()
# album_repository.delete_all()

artist1 = Artist('James Rocker')
artist_repository.save(artist1)
artist2 = Artist('wally')
artist_repository.save(artist2)

album1 = Album('Sing a long', 'HIpHOp', artist1)
album_repository.save(album1)


pdb.set_trace()