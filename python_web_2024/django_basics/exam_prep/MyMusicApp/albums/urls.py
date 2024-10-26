from django.urls import include,path

from albums import views

urlpatterns = [
    path('add/', views.AlbumCreateView.as_view(), name='add-album'),
    path('<int:id>/', include([
        path('edit/', views.AlbumEditView.as_view(), name='album-edit'),
        path('details/', views.AlbumDetailsView.as_view(), name='album-details'),
        path('delete/', views.AlbumDeleteView.as_view(), name='album-delete'),
    ]))
]