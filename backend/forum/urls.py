from django.contrib import admin
from django.urls import path, include
from forum import views

urlpatterns = [
    path('', views.QuestionList.as_view(), name="home"),
    path('question/', views.QuestionCreateView.as_view(), name="question-list"),
    path('question/<int:qid>/', views.QuestionDetailView.as_view(), name="question-details"),
    path('question/answer/<int:qid>/', views.AnswerList.as_view(), name="answer-list"),
    path('answer/<int:aid>/', views.AnswerDetailView.as_view(), name="answer-details"),
    path('upvote/<int:aid>/<int:uid>/', views.Upvote.as_view(), name="upvote"),
    path('getUser/<int:uid>', views.UserDetail.as_view(), name="get-user"),
]
