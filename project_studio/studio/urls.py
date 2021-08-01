from django.urls import path

from project_studio.studio.views import landing_page

urlpatterns = [
    path('', landing_page, name="home"),

]