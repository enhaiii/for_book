from book_app import views
from django.urls import path

urlpatterns = [
    path('main/', views.MainPage.as_view()),
    path('author/<int:pk>', views.AuthorPage.as_view())
]