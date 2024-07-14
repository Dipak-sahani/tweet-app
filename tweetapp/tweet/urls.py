
from django.urls import path
from . import views


urlpatterns = [
    path('index',views.index),
    path('',views.tweet_list,name="list"),
    path('create',views.tweet_create,name="create"),
    path('<int:tweet_id>/edit',views.tweet_edit,name="edit"),
    path('<int:tweet_id>/delete',views.tweet_delete,name="delete"),
    path('register/',views.register,name="register")
] 