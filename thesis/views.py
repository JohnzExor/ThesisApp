from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator


def thesis(request):
    post = Post.objects.all()
    paginator = Paginator(post, 3)
    page_number = request.GET.get("page")
    post = paginator.page(page_number)
    return render(request, "pagination.html", {"post": post})


def thesis_details(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.APPROVED)
    return render(request, "thesis_details.html", {"post": post})
