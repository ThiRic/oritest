from django.contrib import admin

from .models import Question, Choice, Questionnaire, QuestionnaireInstance

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Questionnaire)
admin.site.register(QuestionnaireInstance)