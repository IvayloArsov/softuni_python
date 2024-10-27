from tkinter import Place

from django import forms

from examProj.util import PlaceholderMixin, ReadOnlyMixin
from posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'image_url',
            'content'
        ]


class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Put an attractive and unique title...',
                'required': 'required'
            }),
            'image_url': forms.URLInput(attrs={
                'help': 'Share your funniest furry photo URL!',
                'label': 'Post Image URL:',
                'required': 'required'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Share some interesting facts about your adorable pets...',
                'required': 'required'
            }),
        }


class PostEditForm(PlaceholderMixin, PostBaseForm):
    pass

class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    readonly_fields = [
        'title',
        'image_url',
        'content'
    ]
