"""quant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from pervez import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admins'),
    path('', auth_views.home, name='home-page'),
    path('notes/<int:cls>/', auth_views.Notess, name='notes'),
    path('notes_page/', auth_views.notes_page, name='notes-page'),
    path('papers/<int:cls>/', auth_views.question_answers, name='q-n-a'),
    path('lectures/<int:cls>/', auth_views.lectures_subjects, name='lec-sub'),
    path('paper_page/', auth_views.paper_page, name='paper-page'),
    path('lecture_page/', auth_views.lecture_page, name='lecture-page'),
    # path('vidio_lec/<str:sub>/<str:chap_name>/', auth_views.per_video, name='individual-chapter'),
    path('vidio_lec/<int:pk>/<str:chap_name>/', auth_views.per_video, name='individual-chapter'),
    path('subtopics/<int:pk>/<str:chap_name>/', auth_views.subtopics, name='subtopics-chapter'),
    # path('notes/', auth_views.Notess, name='notes'),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)