# جانجو بتدور من بعد التمبلت


from django.shortcuts import render
from .models import HomePage,ContactPage,AboutPage,Post


def home(request):
    posts=Post.objects.filter(status='PB') #هتجيب البوست اللي مش درافت
    page = HomePage.objects.all()[0]
    return render(request, "blog/home.html",{'page':page , "posts" : posts})


def about(request):
    page = AboutPage.objects.all()[0]
    return render(request, "blog/about.html", {"page": page})


def post(request):
    
    return render(request, "blog/post_details.html")


def contact(request):
    page = ContactPage.objects.all()[0]
    return render(request, "blog/contact.html", {"page": page})
