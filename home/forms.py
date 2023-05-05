from django import forms
from home.models import Speak

class PostForm(forms.ModelForm):
    class Meta:
        model = Speak
        fields = ['who_speaks', 'speak_box']