from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display=["title","updated","time_stamp"]
    list_display_links = ["time_stamp"]
    list_filter = ["updated"]
    search_fields = ["content"]
    class Meta:
        model = Post
admin.site.register(Post,PostModelAdmin)
