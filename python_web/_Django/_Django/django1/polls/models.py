from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField('질문 제목', max_length=200)
    pub_date = models.DateTimeField('입력 날짜')
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('선택 사항', max_length=200)
    votes = models.IntegerField('투표 수', default=0)

    def __str__(self):
        return self.choice_text

        