from django import forms

from .models import Counter

class CountForm(forms.ModelForm):

    class Meta:
        model = Counter
        fields = ('title', 'count',)