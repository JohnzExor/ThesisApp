from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .forms import CommentForm
from django.views.decorators.http import require_POST



def thesis_search(request):
    keyword = request.GET.get("keyword")
    post = Post.objects.filter(
        Q(title__contains=keyword)
        | Q(authors__contains=keyword)
        | Q(abstract__contains=keyword)
    )
    paginator = Paginator(post, 3)
    page_number = request.GET.get("page")
    try:
        post = paginator.page(page_number) 
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, "thesis/pagination.html", {"post": post})

def thesis_list(request):
    post = Post.objects.all()
    paginator = Paginator(post, 3)
    page_number = request.GET.get("page")
    try:
        post = paginator.page(page_number) 
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, "thesis/pagination.html", {"post": post})


def thesis_details(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post,
    )
    comments = post.comments.filter(active=True)
    form = CommentForm()

    return render(request, "thesis/post/detail.html", {"post": post,"comments": comments,
                   "form":form})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    return render(request, "thesis/post/comment.html",
                        {'post': post,
                         'form': form, 
                         'comment': comment})
