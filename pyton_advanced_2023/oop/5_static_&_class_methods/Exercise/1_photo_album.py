class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = (photos_count + 3) // 4
        return cls(pages)

    def add_photo(self, label):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"
        return 'No more free slots'

    def display(self):
        result = ["-" * 11]
        for i in range(len(self.photos)):
            row_len = len(self.photos[i])
            if row_len > 0:
                result.append(("[] " * row_len).rstrip())
            else:
                result.append("")
            result.append("-" * 11)
        return '\n'.join(result)
