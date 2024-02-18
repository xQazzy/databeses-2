from django import forms
from .models import Article, Scope


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'image', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].widget = forms.CheckboxSelectMultiple()

    def clean_tags(self):
        tags = self.cleaned_data['tags']
        if len(tags) < 1:
            raise forms.ValidationError("Должен быть указан хотя бы один тег")
        main_tags_count = sum(1 for tag in tags if Scope.objects.filter(tag=tag, is_main=True).exists())
        if main_tags_count != 1:
            raise forms.ValidationError("Должен быть указан ровно один основной тег")
        return tags
