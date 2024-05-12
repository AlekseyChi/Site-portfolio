from django import forms
from .models import Portfolio

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