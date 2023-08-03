from django.shortcuts import render, reverse
from post.models import Post
from post.forms import PostForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_feed(request):
    posts = Post.objects.all().order_by("-id")
    context = {"posts": posts}
    return render(request, "home_feed.html", context)


def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("post:home"))
    context = {"form" : form}
    return render(request, "add_post.html", context)
