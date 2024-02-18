from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_count = 0
        for form in self.forms:
            if form.cleaned_data:
                is_main = form.cleaned_data.get('is_main')
                if is_main:
                    main_tag_count += 1
                    if main_tag_count > 1:
                        raise ValidationError('Основным может быть только один раздел.')
        if main_tag_count == 0:
            raise ValidationError('Укажите основной раздел.')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
