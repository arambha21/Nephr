"""
nephr_widget/urls.py
"""

from django.urls import path

from nephr_widgets import views

urlpatterns = [
    path("get-filter-form", views.get_filter_form, name="get-filter-form"),
]
