from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.allquestions,name="allquestions"),
    path('askaquestion',views.askaquestion,name="askaquestion"),
    path('answeraquestion/<str:pk>',views.answeraquestion,name="answeraquestion"),
    path("allanswers/<str:pk>",views.allanswers,name="allanswers")
]

