from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from cadeMED.api import viewsets
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

route = routers.DefaultRouter()

route.register (r'clinic',  viewsets.ClinicViweset,basename='Clinic')
route.register (r'specialist', viewsets.SpecialistViewset,basename='Specialist')
route.register (r'category', viewsets.CategoryViewset,basename='Category')
route.register (r'patient', viewsets.PatientViewset,basename='Patient')
route.register (r'schedules', viewsets.SchedulesViewset,basename='Schedules')
route.register (r'historic', viewsets.HistoricViewset,basename='Historic')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(route.urls))
]
