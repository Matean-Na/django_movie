from django.urls import path

from . import views


urlpatterns = [
    path('', views.MoviesView.as_view()),
    path('list/', views.MovieListView.as_view(), name="list"),
    path('filter/', views.FilterMoviesView.as_view(), name='filter'),
    path('search/', views.Search.as_view(), name='search'),
    path('add-rating/', views.AddStarRating.as_view(), name='add_rating'),
    path('celeb/', views.ActorListView.as_view(), name='celeb'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path('list/<slug:slug>/', views.MovieListParamView.as_view(), name="list_param"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
]

