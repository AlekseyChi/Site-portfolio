from django.contrib import admin
from django.contrib.admin import register

from .models import (
    Tag,
    PersonalInfo,
    ProgrammingFramework,
    Language,
    Service,
    Education,
    Qualification,
    WorkReview,
    Award,
    Portfolio,
)
from .forms import (
    TagForm,
    PersonalInfoForm,
    ProgrammingFrameworkForm,
    LanguageForm,
    ServiceForm,
    EducationForm,
    QualificationForm,
    WorkReviewForm,
    AwardForm,
    PortfolioForm,
)

# Register your models here.
@register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio
    form = PortfolioForm
    list_display = ("id", "title", "date", "github_link")
    # list_filter = ("tag")
    

@register(PersonalInfo)
class TagAdmin(admin.ModelAdmin):
    model = PersonalInfo
    form = PersonalInfoForm
    list_display = ("first_name", "last_name")


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    form = TagForm
    list_display = ("name",)