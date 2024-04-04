from django.urls import path

from . import views

urlpatterns = [
    path("products", views.products, name="products"),
    path("faq", views.faq, name="faq"),
    path("about", views.about, name="about"),

]