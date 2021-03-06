# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Question, Answer, SendNotification
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(SendNotification)
