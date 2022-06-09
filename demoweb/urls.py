from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.Vulnerabilityscanner, name="/"),
    # path("Vulnerability-scanner/",views.Vulnerabilityscanner, name="Vulnerability-scanner"),
    path("contact/",views.contact, name="contact"),
    # path("result/",views.result, name="result"),
    path("external/",views.external),
]
