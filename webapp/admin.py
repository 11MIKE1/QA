
from django.contrib import admin
from .models import First_Title, Second_Title, Title, Third_title, Forth_title, Fifth_title, Sixth_title, Seventh_title,Eighth_title,Footer
from django import forms
from django.core.exceptions import ValidationError

admin.site.register(First_Title)
admin.site.register(Second_Title)
admin.site.register(Third_title)
admin.site.register(Forth_title)
admin.site.register(Fifth_title)
admin.site.register(Sixth_title)
admin.site.register(Seventh_title)
admin.site.register(Eighth_title)
admin.site.register(Footer)


class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and Title.objects.exists():
            raise ValidationError("Эта запись уникальна!")

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    form = TitleForm

    