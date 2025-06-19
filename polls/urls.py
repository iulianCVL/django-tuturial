from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("content", views.content, name="content"),
    path("conclusion", views.conclusion, name="conclusion"),

    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("top", views.top_five_questions, name="top_five_questions"),
]