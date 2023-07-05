from django.urls import path
from chatbot import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "webhook/", views.webhook, name="webhook"
    ),  # Make sure the trailing slash is present
]
