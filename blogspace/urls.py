"""
URL configuration for blogspace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from post.views import index,post
from django.urls import path
from django.conf.urls.static import static
from post.views import category,post_category,about
from users.views import register
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name='index'),
    path('posts/',post,name='posts'),
    path('category/',category,name='category'),

    path('post_categories/<int:id>/',post_category,name='post_categories'),

    path('about/',about,name='about'),

    path('register/',register,name='register'),
]
