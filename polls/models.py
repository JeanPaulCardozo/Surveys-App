from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Question(models.Model):
    """Model Question"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """Check if question was published recently"""
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now() 


class Choice(models.Model):
    """Model Choice"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
