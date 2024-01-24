from rest_framework import serializers
from competition.models import Quiz

class QuizSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()
    class Meta:
        model = Quiz
        fields = ['title', 'time_limit', 'active_from', 'active_till', 'difficulty_level','category']
    
    def get_category(self,instance):
        return instance.category.name