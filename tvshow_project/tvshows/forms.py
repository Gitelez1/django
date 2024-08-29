from django import forms
from .models import Show
from datetime import date

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['title', 'network', 'release_date', 'description']

    def clean_release_date(self):
        release_date = self.cleaned_data.get('release_date')
        if release_date and release_date > date.today():
            raise forms.ValidationError('Release date cannot be in the future.')
        return release_date

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description) < 10:
            raise forms.ValidationError('Description must be at least 10 characters long.')
        return description
