from django import template
from ..models import Sections, Subsections, Subsubsections


register = template.Library()


@register.simple_tag()
def get_sections():
    return Sections.objects.filter(draft=False)
    #order by


'''
@register.inclusion_tag('sections/tags/sections_get.html')
def get_subsections(section):
    subsections = Subsections.objects.filter(section=section, draft=False)
    return {"subsections": subsections}


@register.inclusion_tag('sections/tags/sections_get.html')
def get_subsubsections(subsection):
    subsubsections = Subsubsections.objects.filter(section=subsection, draft=False)
    return {"subsubsections": subsubsections}
'''