from django.urls import path
from . import views as core_views
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
    path('', TemplateView.as_view(template_name="core/home.html", extra_context={'activate':'home'}), name="home"),
    path('download', TemplateView.as_view(template_name="core/download.html", extra_context={'activate':'downloads'}), name="download"),
    path('heirarchy', TemplateView.as_view(template_name="core/jsontree.html", extra_context={'activate':'heirarchy'}), name="heirarchy"),
      
]
