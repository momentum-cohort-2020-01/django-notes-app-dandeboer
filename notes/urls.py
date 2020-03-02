from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('admin/', admin.site.urls),
    path('note/<int:pk>', views.note_details, name='note_details'),
    path('post/new/', views.post_new, name='post_new'),
]
