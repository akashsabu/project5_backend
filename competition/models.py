from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "Competition_category"
        verbose_name_plural = "categories"


    def __str__(self):
        return self.name

class Quiz(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    title = models.CharField(max_length=255)
    time_limit = models.DurationField()
    active_from = models.DateTimeField()
    active_till = models.DateTimeField()
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)

    class Meta:
        db_table = "Competition_quiz"
        verbose_name_plural = 'quizzes'

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    text = models.TextField()
    choices = models.JSONField()
    correct_choice = models.IntegerField()

    class Meta:
        db_table = "Competition_questions"

    def __str__(self):
        return self.text


class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        verbose_name_plural = "Leaderboard"
        db_table = "Competition_leaderboard"

    def __str__(self):
        return f'{self.user.username} - {self.quiz.title} - Score: {self.score}'