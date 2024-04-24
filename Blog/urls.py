from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="blog_home"),
    path("about/", views.about, name="about_home"),
    path("contact/", views.contact, name="contact_home"),
    path(
        "post/<int:year>/<int:month>/<int:day>/<slug:post>",
        views.post_detail,
        name="blog_post",
    ),
    path("post/<post_id>/comment", views.post_comment, name="post_comment"),
]
# post/<int:year>/<int:month>/<int:day>/<slug:post>
# احنا بنعمل كدا عشان السيرش وعشانurl يبقا ظاهر فيه الحاجات اللي انا عايزها
