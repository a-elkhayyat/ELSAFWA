"""ONCore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Core.urls')),
    path('patients/', include('Patients.urls')),
    path('lab_test/', include('LabTest.urls')),
    path('radiology/', include('Radiology.urls')),
    path('services/', include('Services.urls')),
    path('medicine/', include('Medicines.urls')),
    path('calendar/', include('Calendar.urls')),
    path('invoices/', include('Invoices.urls')),
    path('physical-therapy/', include('PhysicalTherapy.urls')),
    path('products/', include('Products.urls')),
    path('diet/', include('Diet.urls')),
    path('reports/', include('Reports.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
