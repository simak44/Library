"""
URL configuration for Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from booksapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', views.AuthorView.as_view(), name='author'),
    path('addbook/', views.BookView.as_view(), name='addbook'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('<int:id>', views.BookDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.BookUpdateView.as_view(), name= 'update'),
    path('adelete/<int:id>', views.AuthorDeleteView.as_view(), name='adelete'),
    path('aupdate/<int:pk>', views.AuthorUpdateView.as_view(), name='aupdate'),
    path('aggregation/', views.AggregationView.as_view(), name='aggregation')
]
