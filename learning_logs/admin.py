from django.contrib import admin

from learning_logs.models import Topic, Entry

admin.site.site_header = '学习笔记后台管理系统'
admin.site.site_title = '学习笔记后台'
admin.site.register(Topic)
admin.site.register(Entry)