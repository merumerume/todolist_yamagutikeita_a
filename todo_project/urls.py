from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),  # todo_app の URL 設定をインクルード
]
