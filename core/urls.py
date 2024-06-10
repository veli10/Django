"""
URL configuration for core project.

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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from article.views import *

urlpatterns = [
    path("", home__view, name="home"),
    path("contact", home__view, name="contact"),
    path("about", home__view, name="about"),
    path("articles", articles__view, name="articles"),
    path("article-detail/<int:id>", article_detail_view, name="article-detail"),
    path("addarticles", addarticles__view, name="addarticles"),
    path("update/<int:id>", article__update__view, name="update"),
    path("delete/<int:id>", article__delete__view, name="delete"),
    path("comment/<int:id>", addcomment__view, name="comment"),
    path("dashboard", dashboard__view, name="dashboard"),
    path("account/", include("account.urls")),
    path('admin/', admin.site.urls),
]

handler404 = "article.views.custom_404"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)