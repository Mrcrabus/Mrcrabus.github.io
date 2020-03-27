from django import forms
from .models import News


class NewsImage(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewsImage, self).__init__(*args, **kwargs)
        self.fields['img'].ladel = 'News picture'

    class Meta:
        model = News
        fields = ['img']
