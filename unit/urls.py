"""unit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('home/', views.homepage, name='home'),
    path('lengthview/',views.lengthview,name='convert_length'),
    path('convert_currency/',views.convert_currency,name='convert_currency'),
    path('convert_power/',views.convert_power,name='convert_power'),
    path('convert_Dynamic_Viscocity/',views.convert_Dynamic_Viscocity,name='convert_Dynamic_Viscocity'),
    path('convert_heat_flux/',views.convert_heat_flux,name='convert_heat_flux'),
    path('convert_volume/',views.convert_volume,name='convert_volume'),
    path('convert_energy/',views.convert_energy,name='convert_energy'),
    path('convert_kinematic/',views.convert_kinematic,name='convert_kinematic'),
    path('convert_specific/',views.convert_specific,name='convert_specific'),
    path('convert_molar/',views.convert_molar,name='convert_molar'),
    path('convert_mass/',views.convert_mass,name='convert_mass'),
    path('convert_mass_flowrate/',views.convert_mass_flowrate,name='convert_mass_flowrate'),
    path('convert_specific_heat/',views.convert_specific_heat,name='convert_specific_heat'),
    path('convert_volumetric_flowrate/',views.convert_volumetric_flowrate,name='convert_volumetric_flowrate'),
    path('convert_density/',views.convert_density,name='convert_density'),
    path('convert_area/',views.convert_area,name='convert_area'),
    path('convert_pressure/',views.convert_pressure,name='convert_pressure'),
    path('convert_Heat_Transfer_Coeffcient/',views.convert_Heat_Transfer_Coeffcient,name='convert_Heat_Transfer_Coeffcient'),
    path('convert_Thermal_Conductivity/',views.convert_Thermal_Conductivity,name='convert_Thermal_Conductivity'),


   
]
