"""frontend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path, re_path
from interface import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("/<query>", views.index, name="index"),
    path("sort/<_order>", views.index, name="index"),
    path("download/<pk>", views.download, name="download"),
    path("favorite/<pk>", views.favorite, name="favorite"),
    path("share/<pk>", views.share, name="share"),
    path("share/<pk>", views.info, name="info"),
    path("prev_page/<bookset>", views.prev_page, name="prev_page"),
    path("next_page/<bookset>", views.next_page, name="next_page"),
    path("search/", views.index, name="search"),
    path("search/<query>", views.index, name="search"),
    path("search/<query>/<_set>", views.index, name="search"),
    path("show_collection/<_collection>/<_colset>", views.show_collection, name="show_collection",),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
