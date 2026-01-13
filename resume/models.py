from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True)
    summary_en = models.TextField(blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, help_text="Full LinkedIn URL (https://...)")

    def __str__(self):
        return self.name


class Experience(models.Model):
    profile = models.ForeignKey(Profile, related_name='experiences', on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    company_en = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200)
    role_en = models.CharField(max_length=200, blank=True, null=True)
    start = models.CharField(max_length=50, blank=True)
    end = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    description_en = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.role} @ {self.company}"


class Education(models.Model):
    profile = models.ForeignKey(Profile, related_name='education', on_delete=models.CASCADE)
    institution = models.CharField(max_length=200)
    institution_en = models.CharField(max_length=200, blank=True, null=True)
    degree = models.CharField(max_length=200, blank=True)
    degree_en = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Skill(models.Model):
    profile = models.ForeignKey(Profile, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class ProgrammingSkill(models.Model):
    profile = models.ForeignKey(Profile, related_name='programming_skills', on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    language_en = models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)], help_text="1-5 scale")

    class Meta:
        verbose_name = 'Programozási ismeret'
        verbose_name_plural = 'Programozási ismeretek'

    def __str__(self):
        return f"{self.language} ({self.level})"
