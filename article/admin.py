from django.contrib import admin
from .models import Article, Comment
# Register your models here.

admin.site.register(Article)

admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=["comment_author"]
    list_display_links=["comment_author"]
    list_filter=["created_date"]
    search_fields=["comment_author"]

    class Meta:
        model = Comment
