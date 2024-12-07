"""
URL configuration for polyteacher project.

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
from translator.views import AllTranslationsViewSet
# from translator.views import FrenchSpanishTranslationViewSet
# from translator.views import FrenchEnglishTranslationViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Polyteacher API",
        default_version='v1',
        description="API for Polyteacher",
        terms_of_service="https://www.google.com/policies/terms/",
        ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('redoc', cache_timeout=0)),
    # path('', index),
    path('api/all_translations/', AllTranslationsViewSet.as_view(), name='all_translations'),
    # path('api/french_spanish_translator/', FrenchSpanishTranslationViewSet.as_view(), name='french_spanish_translator'),
    # path('api/french_english_translator/', FrenchEnglishTranslationViewSet.as_view(), name='french_english_translator'),
]
