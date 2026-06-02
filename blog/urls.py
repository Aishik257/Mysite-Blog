from django.urls import path
from . import views 

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.PostView.as_view(), name="post-page"),
    path("posts/<slug:slug>/", views.PostDetailsView.as_view(), name="post-details-page"),
    path("read-later",views.ReadLaterView.as_view(), name="read-later"),
    path('api/posts/', views.PostAPIView.as_view()),
]