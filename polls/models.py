from django.db import models

import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Dane(models.Model):
    rok = models.CharField(max_length=20)
    przychody = models.CharField(max_length=20)
    zysk_brutto = models.CharField(max_length=20)
    dzialalnosc_operacyjna = models.CharField(max_length=20)
    dzialalnosc_finansowa = models.CharField(max_length=20)
    zysk_netto = models.CharField(max_length=20)
    def __str__(self):
        return self.rok
