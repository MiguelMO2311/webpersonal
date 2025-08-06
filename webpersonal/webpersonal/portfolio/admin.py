from django.contrib import admin
from .models import Project, Diploma

# Admin de proyectos
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'created', 'link')
    ordering = ('-created',)

# Admin de diplomas
class DiplomaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'date')
    ordering = ('-date',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Diploma, DiplomaAdmin)
