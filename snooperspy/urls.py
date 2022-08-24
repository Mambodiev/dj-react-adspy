from django.urls import path
from django.views.generic import TemplateView

app_name = 'snooperspy'

urlpatterns = [
    path('', TemplateView.as_view(template_name="snooperspy/index.html")),
]