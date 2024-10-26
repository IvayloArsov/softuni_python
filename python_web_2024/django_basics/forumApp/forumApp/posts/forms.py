from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    # def clean_author(self):
    #     author = self.cleaned_data.get('author')
    #
    #     if not author[0].isupper():
    #         raise ValidationError('Author must be uppercase.')
    #
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     title = cleaned_data.get("title")
    #     content = cleaned_data.get("content")
    #     if title and content and title in content:
    #         raise ValidationError('The post name cannot be included in the post\'s content.')
    #
    def save(self, commit=True):
        post = super().save(commit=False)
        post.title = post.title.capitalize()
        if commit:
            post.save()
        return post


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm, DisableFieldsMixin):
    disabled_fields = (
        'title',
    )
    pass


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a post...',
            }
        )
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'author',
            'content',
        )
        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': 'This field is required.',
            },
            'content': {
                'required': 'This field is required.',
            }
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Y   our name',
            }
        )
        self.fields['content'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Add message...',
            }
        )

CommentFormSet = formset_factory(CommentForm, extra=1)