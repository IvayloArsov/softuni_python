from django.urls import path,include

from authors.views import AuthorCreateView
from posts.views import PostCreateView, PostDetailsView, PostDeleteView, PostEditView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('<int:id>/',include([
        path('details/', PostDetailsView.as_view(), name='details'),
        path('delete/', PostDeleteView.as_view(), name='delete-post'),
        path('edit/', PostEditView.as_view(), name='edit-post'),
    ]))

]