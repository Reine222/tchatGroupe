from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact', 'lien_fb', 'lien_twt', 'lien_insta', 'view_image')
    list_filter = ('user',)
    list_search = ('user')
    ordering = ('user',)
    list_per_page = 5
    def view_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'message', 'date_post', 'date_add', 'date_upd', 'status')
    list_filter = ('date_add', 'date_post', 'date_upd', 'status',)
    list_search = ('utilisateur')
    ordering = ('utilisateur',)
    list_per_page = 5
    actions = ('active', 'desactive',)

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'Activer une Message')
    active.short_description = 'active Message'

    def desactive(self, queryset, request):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Message')
    desactive.short_description = 'desactive Message'



@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'tel', 'view_image')
    list_filter = ('nom',)
    list_search = ('nom')
    ordering = ('nom',)
    list_per_page = 5
    def view_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))

