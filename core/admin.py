from django.contrib import admin
from .models import *


@admin.action(description="Установить изображение по умолчанию")
def set_preview(modeladmin, request, queryset):
    queryset.update(preview="default_images/default_video.png")

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_id', 'url', 'created_at', 'video_for_main')  # Fields to display in the list view
    readonly_fields = ('video_id',)  # Make 'video_id' read-only
    actions = [set_preview]
    def save_model(self, request, obj, form, change):
        if 'url' in form.changed_data:
            match = re.search(r'\?v=([^&]+)', obj.url)
            if match:
                obj.video_id = match.group(1)
        super().save_model(request, obj, form, change)
    
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

@admin.action(description="Установить изображение по умолчанию")
def set_image(modeladmin, request, queryset):
    queryset.update(image="default_images/default_news.png")

class NewsAdmin(admin.ModelAdmin):
    actions = [set_image]
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()



admin.site.register(News, NewsAdmin)
admin.site.register(Comment)
admin.site.register(Video, VideoAdmin)