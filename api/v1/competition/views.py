from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from api.v1.competition.serializers import QuizSerializer
from rest_framework.response import Response
from datetime import datetime

from competition.models import Quiz

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def active_quizzes(request):
    current_datetime = datetime.now()
    active_quizzes = Quiz.objects.all()
    serializer = QuizSerializer(active_quizzes, many=True)
    return Response(serializer.data)
