from django.contrib import admin

from .models import HomePage, AboutPage, ContactPage, Post,Comment


admin.site.register(HomePage)
admin.site.register(AboutPage)
admin.site.register(ContactPage)





@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "created_ad", "status"] # الحقول التي تظهر في قائمة العناصر في صفحة الادمن

    list_filter = ["status", "created_ad", "publish", "author"]    # الحقول التي يمكن استخدامها لتصفية العناصر في صفحة الإدارة

    search_fields = ["title", "body"]        # الحقول التي يمكن البحث عن العناصر بها في صفحة الإدارة

    prepopulated_fields = {"slug": ("title",)}     # توليد قيمة slug تلقائيًا باستخدام قيمة عنوان المقالة

    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ["status", "publish"]     # الترتيب الافتراضي للعناصر في صفحة الإدارة حسب حالتها ثم تاريخ النشر


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "created_at",
        "active",
        "body",
        
    ]  # الحقول التي تظهر في قائمة العناصر في صفحة الادمن

    list_filter = [
        "active",
        "created_at",
        
    ]  # الحقول التي يمكن استخدامها لتصفية العناصر في صفحة الإدارة

    search_fields = [
        "name",
        "body",
        "active",
    ]  # الحقول التي يمكن البحث عن العناصر بها في صفحة الإدارة

   