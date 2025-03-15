"""
URL configuration for Japassists project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from tool01 import views

app_name = "tool01"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),  # 根路径显示首页

    # 日语汉字转假名小工具
    path('jap_kanji/', views.japan_kanji, name='jap_kanji_hira'),

    # 日语语音识别小工具
    path('jap_audio_rec/', views.jap_audio_rec, name='jap_audio_rec'),
]
