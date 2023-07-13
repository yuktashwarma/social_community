from django.urls import path
from django_social_app.models import *
from django_social_app.views import userView

urlpatterns = [
    path("user/view/", userView.GetUserAPIView.as_view(),name="user_list"),
    #path("user/create/", userView.CreateUserAPIView.as_view(),name="create_user"),
    #path("user/update/<int:pk>/",User.UpdateTodoAPIView.as_view(),name="update_user"),
    #path("user/deactivate/<int:pk>/",User.DeleteTodoAPIView.as_view(),name="deactivate_user")
]