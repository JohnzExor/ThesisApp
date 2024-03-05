from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator


def thesis(request):
    post = Post.objects.all()
    paginator = Paginator(post, 3)
    page_number = request.GET.get("page")
    post = paginator.page(page_number)
    return render(request, "thesis/pagination.html", {"post": post})


def thesis_details(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.APPROVED,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post,
    )
    return render(request, "thesis/details.html", {"post": post})


def landing_page(request):
    return render(
        request,
        "home.html",
    )
