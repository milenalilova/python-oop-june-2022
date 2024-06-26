from classes_and_objects_exercise_revision.project.song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.song = args
        self.published = False
        self.songs = []

        for song in args:
            self.songs.append(song)

    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        output = f"Album {self.name}\n"
        for song in self.songs:
            output += f"== {song.get_info()}\n"
        return output.strip()
