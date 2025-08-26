from rest_framework import viewsets, permissions
from .serializers import ScoreSerializer
from main.models.score import Score
class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.order_by("-created_at")
    serializer_class = ScoreSerializer
    permission_classes = [permissions.AllowAny]  # thử nghiệm; sau chuyển sang IsAuthenticated
