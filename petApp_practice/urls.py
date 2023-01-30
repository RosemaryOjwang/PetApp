from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:id>/', views.pet_details, name="pet_details")
]
urlpatterns += staticfiles_urlpatterns()