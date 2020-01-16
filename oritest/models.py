from django.db import models
from django.contrib.auth.models import User

class Questionnaire(models.Model):
    questionnaire_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.questionnaire_text

class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete = models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    C1 = models.IntegerField(default=0)
    C2 = models.IntegerField(default=0)
    C3 = models.IntegerField(default=0)
    C4 = models.IntegerField(default=0)
    E1 = models.IntegerField(default=0)
    E2 = models.IntegerField(default=0)
    S1 = models.IntegerField(default=0)
    S2 = models.IntegerField(default=0)
    S3 = models.IntegerField(default=0)
    S4 = models.IntegerField(default=0)
    S5 = models.IntegerField(default=0)
    D1 = models.IntegerField(default=0)
    D2 = models.IntegerField(default=0)
    D3 = models.IntegerField(default=0)
    D4 = models.IntegerField(default=0)
    D5 = models.IntegerField(default=0)
    D6 = models.IntegerField(default=0)
    N1 = models.IntegerField(default=0)
    N2 = models.IntegerField(default=0)
    N3 = models.IntegerField(default=0)
    N4 = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class QuestionnaireInstance(models.Model):
    '''A combination of user response and a questionnaire template, taken from: https://github.com/badri/django-quiz/blob/master/models.py'''
    taker = models.ForeignKey(User, on_delete = models.CASCADE)
    questionnaire_taken = models.ForeignKey(Questionnaire, on_delete = models.CASCADE)
    C1_score = models.IntegerField(default=0)
    C2_score = models.IntegerField(default=0)
    C3_score = models.IntegerField(default=0)
    C4_score = models.IntegerField(default=0)
    E1_score = models.IntegerField(default=0)
    E2_score = models.IntegerField(default=0)
    S1_score = models.IntegerField(default=0)
    S2_score = models.IntegerField(default=0)
    S3_score = models.IntegerField(default=0)
    S4_score = models.IntegerField(default=0)
    S5_score = models.IntegerField(default=0)
    D1_score = models.IntegerField(default=0)
    D2_score = models.IntegerField(default=0)
    D3_score = models.IntegerField(default=0)
    D4_score = models.IntegerField(default=0)
    D5_score = models.IntegerField(default=0)
    D6_score = models.IntegerField(default=0)
    N1_score = models.IntegerField(default=0)
    N2_score = models.IntegerField(default=0)
    N3_score = models.IntegerField(default=0)
    N4_score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.taker)