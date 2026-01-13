from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from .models import Profile, Experience, Education, Skill, ProgrammingSkill


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start', 'end')


class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year')


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')


class ProgrammingSkillAdmin(admin.ModelAdmin):
    list_display = ('language', 'level', 'profile')


for model, admin_class in (
    (Profile, ProfileAdmin),
    (Experience, ExperienceAdmin),
    (Education, EducationAdmin),
    (Skill, SkillAdmin),
    (ProgrammingSkill, ProgrammingSkillAdmin),
):
    try:
        admin.site.register(model, admin_class)
    except AlreadyRegistered:
        pass
