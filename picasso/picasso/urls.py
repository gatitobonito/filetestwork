"""picasso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path, re_path

from rest_framework.routers import SimpleRouter

from picfile.views import FileViewSet, UploadViewSet, file_upload

# v1_router = SimpleRouter()

# v1_router.register('files', FileViewSet)
# v1_router.register('upload', UploadViewSet)
# v1_router.register('upload', FileAPIView.as_view(), basename='upload')

urlpatterns = [
    path('', include(v1_router.urls)),
    # re_path(r'^upload1/$', file_upload, name='file_upload'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)