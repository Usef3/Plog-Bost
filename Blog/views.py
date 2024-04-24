# جانجو بتدور من بعد التمبلت


from django.shortcuts import render,get_object_or_404
from .models import HomePage, ContactPage, AboutPage, Post
from .forms import CommentForm

def home(request):
    posts=Post.objects.filter(status='PB') #هتجيب البوست اللي مش درافت
    page = HomePage.objects.all()[0]
    return render(request, "blog/home.html",{'page':page , "posts" : posts})


def about(request):
    page = AboutPage.objects.all()[0]
    return render(request, "blog/about.html", {"page": page})


def contact(request):
    page = ContactPage.objects.all()[0]
    return render(request, "blog/contact.html", {"page": page})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post,
    )
    comments = post.comments.filter(active=True)
    return render(
        request, "blog/post_details.html", {"post": post, "comments": comments}
    )


def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    comment = None

    form = CommentForm(data=request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    return render(
        request, "blog/comment.html", {"comment": comment, "form": form, "post": post}
    )
