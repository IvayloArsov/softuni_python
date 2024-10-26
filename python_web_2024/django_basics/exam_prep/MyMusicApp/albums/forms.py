from albums.models import Album
from django import forms

from MyMusicApp.mixins import PlaceholderMixin, ReadOnlyMixin


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)

class AlbumCreateForm(PlaceholderMixin, AlbumBaseForm):
    pass

class AlbumEditForm(PlaceholderMixin, AlbumBaseForm):
    pass

class AlbumDeleteForm(ReadOnlyMixin, AlbumBaseForm):
    readonly_fields = [
        'album_name',
        'artist',
        'genre',
        'price',
        'description',
    ]
