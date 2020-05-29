from django import template
from ..models import Sticker, Fontans


register = template.Library()


@register.inclusion_tag('df2020/tags/stickers_tag.html')
def get_stickers():
    queryset = Sticker.objects.filter(draft=False).order_by('-id')[:100]
    return {"stickers": queryset}


@register.inclusion_tag('df2020/tags/fontans_tag.html')
def get_fontans():
    queryset = Fontans.objects.filter(draft=False).order_by('-id')
    return {"fontans": queryset}
