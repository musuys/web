"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import board.views
import product.views
import reply.views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.mainPage),
    path('product/create', product.views.createFruitGet),
    path('product/createPost', product.views.createFruitPost),
    path('product/list', product.views.readFruitGet),

    path('board/create', board.views.create),
    path('board/list', board.views.listGet),
    path('board/read/<int:bid>', board.views.readGet),
    path('board/delete/<int:bid>', board.views.deleteGet),
    path('board/update/<int:bid>', board.views.update),

    path('reply/create/<int:bid>', reply.views.create),
    path('reply/list', reply.views.list),
    path('reply/read/<int:rid>', reply.views.read),
    path('reply/delete/<int:rid>', reply.views.delete),
    path('reply/update/<int:rid>', reply.views.update),

    path('user/signup', user.views.signup),
    path('user/login', user.views.login),
    path('user/logout', user.views.logout),

    path('like/<int:bid>', board.views.like),

]
