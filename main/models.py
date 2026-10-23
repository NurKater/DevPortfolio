from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=5)
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text="Comma-separated", default="")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text="Comma-separated", default="")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank if currently working")

    def __str__(self):
        return f"{self.role} at {self.company}"

