from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "►Тэги"
        unique_together = (("name"),)

    def __str__(self):
        return self.name


class PersonalInfo(models.Model):
    """
    Персональная информация пользователя
    """
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

    class Meta:
        verbose_name = "Персональная информация"
        verbose_name_plural = "►Персональная информация"
        unique_together = (("vk_link", "tg_link", "github_link", "linkedin_link"),)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ProgrammingFramework(models.Model):
    """
    Список фреймворков
    fields = ["id", "name", "personal_info"]
    """
    name = models.CharField(max_length=100)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Фреймворки"
        verbose_name_plural = "►Фреймворк"
        unique_together = (("name"),)

    def __str__(self):
        return self.name


class Language(models.Model):
    """
    Международные языки
    fields = ["id", "name", "language_level", "personal_info"]
    """
    name = models.CharField(max_length=100)
    language_level = models.IntegerField(validators=[MaxValueValidator(100)], null=True) 
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Языки"
        verbose_name_plural = "►Международный язык"
        unique_together = (("name"),)

    def __str__(self):
        return self.name


class Service(models.Model):
    """
    Справочник услуг
    fields = ["id", "name", "personal_info"]
    """
    name = models.CharField(max_length=100)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуга"
        unique_together = (("name"),)

    def __str__(self):
        return self.name


class Education(models.Model):
    """
    Образование
    fields = ["id", "institution", "start_date", "end_date", "certificate_path", "description", "personal_info"]
    """
    institution = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    certificate_path = models.CharField(max_length=255)
    description = models.TextField()
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "►Образование"
        unique_together = (("certificate_path"),)

    def __str__(self):
        return self.institution


class Qualification(models.Model):
    """
    Опыт работы
    fields = ["id", "workplace", "start_date", "end_date", "description", "personal_info"]
    """
    workplace = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "►Опыт работы"

    def __str__(self):
        return self.workplace


class WorkReview(models.Model):
    """
    Отзывы
    fields = ["id", "employer_info", "review_text", "personal_info"]
    """
    employer_info = models.CharField(max_length=255)
    review_text = models.TextField()
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "►Отзыв"

    def __str__(self):
        return self.employer_info


class Award(models.Model):
    """
    Достижения
    fields = ["id", "name", "date", "description", "personal_info"]
    """
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Достижения"
        verbose_name_plural = "►Достижение"

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    """
    Портфолио
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    technologies = models.CharField(max_length=255)
    date = models.DateField()
    customer = models.CharField(max_length=100)
    photo_path = models.CharField(max_length=255, null=False)
    tag = models.ManyToManyField(Tag)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "►Портфолио"
        unique_together = (("github_link"),)

    def __str__(self):
        return self.title
