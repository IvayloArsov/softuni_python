from django.urls import path

from authors.views import AuthorCreateView, AuthorDetailView, AuthorDeleteView, AuthorEditView

urlpatterns = [
    path('details/', AuthorDetailView.as_view(), name='author-details'),
    path('delete/',AuthorDeleteView.as_view(), name='author-delete'),
    path('edit/',AuthorEditView.as_view(), name='author-edit'),
    path('create/', AuthorCreateView.as_view(), name='author-create'),
]