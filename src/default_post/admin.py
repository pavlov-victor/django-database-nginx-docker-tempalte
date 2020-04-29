from django.contrib import admin

from default_post.models import DefaultPost


@admin.register(DefaultPost)
class DefaultPostAdmin(admin.ModelAdmin):
    pass
