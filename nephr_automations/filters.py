"""
nephr_automations/filters.py
"""

from nephr.filters import NephrFilterSet, django_filters
from nephr_automations.models import MailAutomation


class AutomationFilter(NephrFilterSet):
    """
    AutomationFilter
    """

    search = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = MailAutomation
        fields = "__all__"
