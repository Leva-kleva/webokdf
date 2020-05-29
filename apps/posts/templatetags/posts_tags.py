from django import template
from ..models import *
from ...sections.models import *

register = template.Library()


@register.inclusion_tag('posts/tags/posts_tag.html')
def get_posts(request):
    tmp = request.META['PATH_INFO'].split('/')[2:-1]
    #while len(tmp) < 4:
    #    tmp.append('NULL')
    obj = []
    if len(tmp) == 0:
        queryset = Post.objects.filter(draft=False).order_by("-order")
    if len(tmp) == 1:
        obj.append(Sections.objects.get(url=tmp[0], draft=False))
        queryset = Post.objects.filter(section=obj[0], draft=False).order_by("-order")
    if len(tmp) == 2:
        obj.append(Sections.objects.get(url=tmp[0], draft=False))
        obj.append(Subsections.objects.get(url=tmp[1], draft=False))
        queryset = Post.objects.filter(section=obj[0], subsection=obj[1], draft=False).order_by("-order")
    if len(tmp) == 3:
        obj.append(Sections.objects.get(url=tmp[0], draft=False))
        obj.append(Subsections.objects.get(url=tmp[1], draft=False))
        obj.append(Subsubsections.objects.get(url=tmp[2], draft=False))
        queryset = Post.objects.filter(
            section=obj[0], subsection=obj[1], subsubsection=obj[2], draft=False
        ).order_by("-order")

    return {"posts": queryset}
