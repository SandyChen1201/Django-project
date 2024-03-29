"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views

# 產生路由/分配User次要路徑
urlpatterns = [
    # 為了redirect或方便查找本地網址，一定要有替代名車
    # 空對空才會變成首頁
    path("", views.todolist, name="todolist"),
    path("todo/<int:id>", views.view_todo, name="view_todo"),
    path("create-todo/", views.create_todo, name="create_todo"),
    path("completed-todo/", views.completed_todo, name="completed_todo"),
    path("delete-todo/<int:id>", views.delete_todo, name="delete_todo"),
    path("finish-todo/<int:id>", views.finish_todo, name="finish_todo"),
    path("recover-todo/<int:id>", views.recover_todo, name="recover_todo"),
]
