from django.contrib import admin
from .models import Project, Skill, Experience

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'github_url')
    search_fields = ('title', 'technologies')
    list_filter = ('created_at',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'category')
    list_filter = ('category', 'level')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'role', 'start_date', 'end_date')
    search_fields = ('company', 'role')

