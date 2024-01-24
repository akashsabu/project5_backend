from django.contrib import admin
from competition.models import Category,Quiz,Question,Options,Leaderboard


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_limit', 'active_from', 'active_till', 'difficulty_level','category']


class OptionsInline(admin.TabularInline):
     model = Options

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text' ]
    inlines = [OptionsInline]


class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'score']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Options)
admin.site.register(Leaderboard, LeaderboardAdmin)
