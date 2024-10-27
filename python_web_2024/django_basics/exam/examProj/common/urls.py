from common.views import HomePage, DashboardPage
from django.urls import path

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('dashboard/', DashboardPage.as_view(), name='dashboard'),
]
