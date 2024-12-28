from django.urls import path
from .views import landing_page, dashboard_landing_page

urlpatterns = [
    path('', landing_page, name="landing_page"),
    path('dashboard/', dashboard_landing_page, name="dashboard_landing_page"),
]