from django.urls import path
from . import views

# Se coloca nombre de app para distinguir las rutas
# que tengan nombre iguales en las apps
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.votes, name="vote"),
]


