from django.urls import path

from washes import views

app_name = 'washes'

urlpatterns = [
    path('washes/', views.WashList.as_view()),
    path('wash/<int:pk>/', views.WashDetail.as_view())
]