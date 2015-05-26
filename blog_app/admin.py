from django.contrib import admin

from .models import Post, Comment

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Введите заголовок новости', {'fields': ['post_title']}),
        ('Введите текст новости', {'fields': ['post_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]
    list_display = ('post_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['post_text']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
