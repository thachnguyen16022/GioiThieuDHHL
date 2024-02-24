"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home import views as home
from django.conf.urls.static import static
from  django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.get_home),
    path('lich-su-thanh-lap/',home.get_gioithieu1),
    path('su-mang-va-muc-tieu/',home.get_gioithieu2),
    path('so-do-co-cau-to-chuc/',home.get_gioithieu3),
    path('ban-giam-hieu/',home.get_gioithieu4),
    path('addCmt',home.add_comments),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header="DHHL QUẢN TRỊ VIÊN"
