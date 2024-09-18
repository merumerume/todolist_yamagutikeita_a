from django.contrib import admin
from .models import Tag, TodoList  # Category を削除

admin.site.register(Tag)
admin.site.register(TodoList)
