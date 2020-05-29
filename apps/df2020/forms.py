from django import forms
#from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Sticker, Fontans, History

class StickerForm(forms.ModelForm):
    #captcha = ReCaptchaField()

    class Meta:
        model = Sticker
        fields = ("description", "color")


class FontanForm(forms.ModelForm):
    #captcha = ReCaptchaField()

    class Meta:
        model = Fontans
        fields = ("name", "description", "link")


class HistoryForm(forms.ModelForm):
    #captcha = ReCaptchaField()

    class Meta:
        model = History
        fields = ("description",)


'''class ZagsForm(forms.ModelForm):
    #captcha = ReCaptchaField()

    class Meta:
        model = Zags
        fields = ("type", "name1", "name2")'''
