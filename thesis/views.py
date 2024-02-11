from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def thesis(request):
    post = Post.objects.all()
    return render(request, "index.html", {"post": post})
