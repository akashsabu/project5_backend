from django.urls import path,include
from api.v1.competition import views


urlpatterns = [
    path('active_quizzes/', views.active_quizzes, name='active_quizzes'),

]
