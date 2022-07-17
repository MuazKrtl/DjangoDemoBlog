from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard,name="dashboard"),
    path('addarticle/', views.addArticle,name="addArticle"),
    path('article/<int:id>',views.detail,name="detail"),
    path('delete/<int:id>',views.deleteArticle,name="deleteArticle"),
    path('update/<int:id>',views.updateArticle,name="updateArticle"),
    path('',views.articles,name="articles"),
    path('comment/<int:id>',views.addComment,name="comment"),
]
