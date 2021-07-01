from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    #<esto siempre es una cadena de carcteres los parametros dinamicos se detectan como parametros>
    #pero si agg init:
    path('category/<int:category_id>/', views.category, name="category"),
]