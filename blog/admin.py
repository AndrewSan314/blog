from django.contrib import admin
from .models import Post, Comment
from django.contrib.admin import ModelAdmin


# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3


class PostAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['author'], 'fields': ['text']}),
        ('Date information', {'fields': ['publish_date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)
