from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'
        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        found_album = None

        for album in self.albums:
            if album.name == album_name:
                found_album = album
                break

        if found_album is None:
            return f'Album {album_name} is not found.'

        if found_album.published:
            return 'Album has been published. It cannot be removed.'

        self.albums.remove(found_album)
        return f'Album {found_album.name} has been removed.'

    def details(self):
        info_str = [f'Band {self.name}']
        for album in self.albums:
            info_str.append(f'{album.details()}')
        return '\n'.join(info_str)


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
