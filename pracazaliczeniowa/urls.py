"""pracazaliczeniowa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from bookingyacht import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
    path("", views.IndexView.as_view(), name='index'),
    path("view_yacht/", views.YachtPersonView.as_view(), name='view_yacht'),
    path("add_yacht/", views.AddYacht.as_view(), name='add_yacht'),
    path("yacht_detail/<int:id>/", views.YachtViewDetail.as_view(), name="yacht_details"),
    path("update_yacht/<int:pk>/", views.UpdateYacht.as_view(), name="yacht_update"),
    path('view_yacht/delete/<int:id>/', views.DeleteYacht.as_view(), name="delete-yacht"),
    path("delete/<int:id>/", views.DeleteYacht.as_view(), name='delete_yacht'),
]
