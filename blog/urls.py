from blog.views import post_detail
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("webhook/", views.webhook),
]
