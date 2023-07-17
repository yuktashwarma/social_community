from django.urls import path
from django_social_app.models import *
from django_social_app.views import user_view
from django_social_app.views import drama_view
from django_social_app.views import like_view
from django_social_app.views import comment_view

urlpatterns = [
    path("user/view/", user_view.GetUserAPIView.as_view(),name="get_user"),
    path("user/create/", user_view.CreateUserAPIView.as_view(),name="create_user"),
    path("drama/view/", drama_view.GetDramaAPIView.as_view(),name="get_drama"),
    path("drama/create/", drama_view.CreateDramaAPIView.as_view(),name="create_drama"),
    path("drama/like/", like_view.AddLikeAPIView.as_view(),name="create_drama"),
    #path("user/update/<int:pk>/",User.UpdateTodoAPIView.as_view(),name="update_user"),
    #path("user/deactivate/<int:pk>/",User.DeleteTodoAPIView.as_view(),name="deactivate_user")
]