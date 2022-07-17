from django.contrib import admin
from .models import Article,Comment
# Register your models here.
admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display= ["author","title"]
    list_display_links= ["title"]
    search_fields = ["title"]
    list_filter = ["created_date"]



    class Meta: #Meta olmak zorunda
        model = Article
