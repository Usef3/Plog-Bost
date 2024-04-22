from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="blog_home"),
    path("about/", views.about, name="about_home"),
    path("contact/", views.contact, name="contact_home"),
    path("post/", views.post, name="post_home"),
]
