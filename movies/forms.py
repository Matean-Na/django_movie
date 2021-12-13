from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Reviews, Rating, RatingStar


class ReviewForm(forms.ModelForm):
    """Форма отзыва"""
    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ("name", "email", "text", "captcha")
        widgets = {
            "name": forms.TextInput(),
            "email": forms.EmailInput(),
            "text": forms.Textarea()
        }


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        # widget - это то как выглядит форма
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)
