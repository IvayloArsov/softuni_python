from project.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.published = False
        self.songs = list(args)

    def add_song(self, song: Song):
        if self.published:
            return 'Cannot add songs. Album is published.'
        if song in self.songs:
            return 'Song is already in the album.'
        if song.single:
            return f'Cannot add {song.name}. It\'s a single'
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if all(song.name != song_name for song in self.songs):
            return 'Song is not in the album.'
        if self.published:
            return 'Cannot remove songs. Album is published.'
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f'Removed song {song_name} from album {self.name}.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        info_str = [f'Album {self.name}']
        for song in self.songs:
            info_str.append(f'=={song.get_info()}')
        return '\n'.join(info_str)
