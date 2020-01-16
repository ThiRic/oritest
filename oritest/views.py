from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Question, Questionnaire, Choice, QuestionnaireInstance

def index(request):
    latest_questionnaire_list = Questionnaire.objects.order_by('-pub_date')[:5]
    template = loader.get_template('oritest/index.html')
    context = {
        'latest_questionnaire_list': latest_questionnaire_list
    }
    return HttpResponse(template.render(context,request))

def detail (request):
    latest_question_list = Question.objects.all()
    template = loader.get_template('oritest/detail.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))

def results (request):
    questionnaire_instance = QuestionnaireInstance.objects.get(taker=request.user)
    answer_instance = Choice.objects.all()
    template = loader.get_template('oritest/results.html')
    context = {}

   # if request.method == 'POST':
   #    questionnaire_instance.C1_score=+ answer_instance.values('C1')



    return HttpResponse(template.render(context,request))
