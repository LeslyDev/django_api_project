from django.contrib import admin
from django.utils.safestring import mark_safe
from english_learning.models import *
# from audiofield.admin import AudioFileAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_tag')
    readonly_fields = ('icon_tag',)

    def icon_tag(self, obj):
        return mark_safe(f'<img src={obj.icon.url} width="50" height="50"')

    icon_tag.short_description = 'Изображение'


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'icon_tag')
    readonly_fields = ('icon_tag',)

    def icon_tag(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="50"')

    icon_tag.short_description = 'Изображение'


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'transcription', 'translation', 'audio_file_player', 'example')
    # actions = ['custom_delete_selected']
    #
    # def custom_delete_selected(self, request, queryset):
    #     # custom delete code
    #     n = queryset.count()
    #     for i in queryset:
    #         if i.audio_file:
    #             if os.path.exists(i.audio_file.path):
    #                 os.remove(i.audio_file.path)
    #         i.delete()
    #     self.message_user(request,
    #                       ("Successfully deleted %d audio files.") % n)
    #
    # custom_delete_selected.short_description = "Delete selected items"

    # def get_actions(self, request):
    #     actions = super(AudioFileAdmin, self).get_actions(request)
    #     del actions['delete_selected']
    #     return actions

