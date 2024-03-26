# Khởi chạy dự án chạy vào đây đầu tiên
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    # tìm tới thu mục urls trong app
    path('', include('DemoApp.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
