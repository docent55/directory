from django.urls import path
from . import views


urlpatterns = [
    path('profile/<int:pk>/', views.UserProfileView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('<int:pk>/', views.UserProfilePublicView.as_view({'get': 'retrieve'}))
]