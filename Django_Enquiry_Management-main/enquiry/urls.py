from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("about/", views.about, name="about"),

    path("contact/", views.contact, name="contact"),

    path("enquiry/", views.enquiry, name="enquiry"),

    path("list/", views.enquiry_list, name="list"),

    path("edit/<int:id>/", views.edit_enquiry, name="edit"),

    path("delete/<int:id>/", views.delete_enquiry, name="delete"),

    path("success/", views.success, name="success"),
]