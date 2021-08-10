from django.contrib import admin
from .models import Contact, Testimonial, Works, Categorey
# Register your models here.
class WorksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','is_published','clients')
    list_display_links = ('id', 'title',)
    list_editable = ('is_published',)
    search_fields = ('title',)
class CategoreyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email_from')
    list_display_links = ('id', 'name',)    
admin.site.register(Works,WorksAdmin)

admin.site.register(Categorey, CategoreyAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Testimonial)