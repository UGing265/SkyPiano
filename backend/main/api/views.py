from rest_framework import viewsets, permissions
from .serializers import ScoreSerializer
from main.models.score import Score
class ScoreViewSet(viewsets.ModelViewSet):
# backend/main/api/serializers.py

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["id", "title", "value", "created_at"]
        read_only_fields = ("id", "created_at")
