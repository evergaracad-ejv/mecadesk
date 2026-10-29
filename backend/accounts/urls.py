from django.urls import path
from .views import dashboard_admin_view, dashboard_gestor_view, dashboard_mecanico_view

urlpatterns = [
    path('dashboard/admin/', dashboard_admin_view, name='dashboard_admin'),
    path('dashboard/gestor/', dashboard_gestor_view, name='dashboard_gestor'),
    path('dashboard/mecanico/', dashboard_mecanico_view, name='dashboard_mecanico'),
]