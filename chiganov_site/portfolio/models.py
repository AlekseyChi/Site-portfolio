from django.db import models

# Create your models here.
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    vk_link = models.URLField(blank=True)
    tg_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ProgrammingFramework(models.Model):
    name = models.CharField(max_length=100)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    certificate_path = models.CharField(max_length=255)
    description = models.TextField()
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.institution

class Qualification(models.Model):
    workplace = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.workplace

class WorkReview(models.Model):
    employer_info = models.CharField(max_length=255)
    review_text = models.TextField()
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.employer_info

class Award(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    technologies = models.CharField(max_length=255)
    date = models.DateField()
    customer = models.CharField(max_length=100)
    photo_path = models.CharField(max_length=255)
    tag = models.ManyToManyField(Tag)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
