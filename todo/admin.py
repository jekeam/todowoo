from django.contrib import admin

from .models import Todo


class TodoAdmnin(admin.ModelAdmin):
    readonly_fields = ('created', )




admin.site.register(Todo, TodoAdmnin)



