from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Questionnaire(models.Model):
    questionnaire_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.questionnaire_name

class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, default=1)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    score_1 = models.IntegerField(default=0, blank=True, null=True) #set for a given answer, the value will be added to Skin_type.score_1
    score_2 = models.IntegerField(default=0, blank=True, null=True)
    score_3 = models.IntegerField(default=0, blank=True, null=True)
    score_4 = models.IntegerField(default=0, blank=True, null=True)
    score_5 = models.IntegerField(default=0, blank=True, null=True)


    def __str__(self):
        return self.answer_text

class Skin_score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score_1 = models.IntegerField(default=0) #will store the final score of the user
    score_2 = models.IntegerField(default=0)
    score_3 = models.IntegerField(default=0)
    score_4 = models.IntegerField(default=0)
    score_5 = models.IntegerField(default=0)