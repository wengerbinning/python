from django.contrib import admin

from .models import Question
# @think: .models why not models?

admin.site.register(Question) 
