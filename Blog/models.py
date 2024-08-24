from django.db import models
from PIL import Image  # بتهندل  الصورة
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone 
from django.urls import reverse


def validate_image_dimensions(image):
    min_width = 1000
    min_height = 500
    img = Image.open(image)    
    width, height = img.size

    if width < min_width or height < min_height:
        raise ValidationError(
            f"Image dimensions must be at least {min_width}px wide and {min_height}px tall."
        )


class PagePase(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=250)
    bg_img = models.ImageField(
        upload_to="imges/%y/%m/%d", validators=[validate_image_dimensions]
    )  # check
    created_ad = models.DateField(auto_now=True)
    updated_ad = models.DateField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class HomePage(PagePase):
    pass


class AboutPage(PagePase):
    description = models.TextField()


class ContactPage(PagePase):
    description = models.TextField()


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT=('DF','Draft')
        PUBLISHED=('PB','Published')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author=models.ForeignKey(User, on_delete=models.CASCADE)  #ريليشن بين البوست واليوزر ميني تو وان من جهة البوست هون دليت عشان لو اليوزر اتمسح البوستات تتمسح
    body=models.TextField()
    bg_img = models.ImageField( upload_to="imges/%y/%m/%d/bg_img")
    post_img = models.ImageField(upload_to="imges/%y/%m/%d/post_img")
    created_ad = models.DateField(auto_now=True)
    updated_ad = models.DateField(auto_now=True)
    publish=models.DateField( default=timezone.now)
    status=models.CharField( max_length=2,choices=Status,default=Status.DRAFT)
    class meta:
        ordering = ['-publish']
        # عشان نعرض البوستس من الحدث للاقدم
        indexes = models.Index(fields=['-publish'])  # تهندل الداتا ف قواعد البيانات
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_post",args=
                       [self.publish.year,
                   self.publish.month,
                     self.publish.day,
                       self.slug]
        )


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=150)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)


class Meta:
    ordering = ["-created_at"]

    indexes = [models.Index(fields=["-created_at"])]

    def __str__(self):
        return f"Comment by {self.name} on post {self.post}"


