from django.contrib import admin
from .models import Works, Categorey
# Register your models here.
class WorksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','is_published','clients')
    list_display_links = ('id', 'title',)
    list_editable = ('is_published',)
    search_fields = ('title',)
class CategoreyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    
    
admin.site.register(Works,WorksAdmin)

admin.site.register(Categorey, CategoreyAdmin)