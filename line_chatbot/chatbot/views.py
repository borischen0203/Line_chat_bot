from django.shortcuts import render

# # Create your views here.
from django.http import HttpResponse
from line_chatbot.line_handler import line_webhook


def index(request):
    return HttpResponse("Hello, this is a Line chat bot.")


def webhook(request):
    if request.method == "POST":
        return line_webhook(request)
    else:
        return HttpResponse(status=400)
