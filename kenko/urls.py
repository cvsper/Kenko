"""kenko URL Configuration

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
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

from kenkoapp import views, apis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('carepro/sign-in', auth_views.login, {'template_name': 'carepro/sign_in.html'}, name='carepro-sign-in'),
    path('carepro/sign-out', auth_views.logout, {'next_page': 'carepro/sign_in.html'}, name='carepro-sign-out'),
    path('carepro', views.carepro_home, name='carepro-home'),
    path('carepro/sign-up', views.carepro_sign_up, name='carepro-sign-up'),
    path('carepro/account', views.carepro_account, name='carepro-account'),
    path('carepro/report', views.carepro_report, name='carepro-report'),
    path('carepro/order', views.carepro_order, name='carepro-order'),

    path('carepro/care', views.carepro_care, name='carepro-care'),
    path('carepro/care/add/', views.carepro_add_care, name='carepro-add-care'),
    path('carepro/care/edit/(?P<care_id>\d+)/$>', views.carepro_edit_care, name='carepro-edit-care'),
    
    path('api/social/', include('rest_framework_social_oauth2.urls')),
    # convert-token sign up & sign up
    # revoke-token sign out

    path('api/customer/carepro/', apis.customer_get_carepro),

] + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
