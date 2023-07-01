from django.contrib import admin
from .models import Question,Answer


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    # ordering = ['-create_date']

class AnswerAdmin(admin.ModelAdmin):
    pass
    # ordering = ['-create_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
