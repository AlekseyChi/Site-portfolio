from django import forms
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
    Portfolio
)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'


class ProgrammingFrameworkForm(forms.ModelForm):
    class Meta:
        model = ProgrammingFramework
        fields = '__all__'


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'


class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__'


class WorkReviewForm(forms.ModelForm):
    class Meta:
        model = WorkReview
        fields = '__all__'


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'

    photo_path = forms.ImageField(label='Фото', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.photo_path:
            self.fields['photo_path'].widget.attrs['readonly'] = True
            self.fields['photo_path'].widget.attrs['disabled'] = True