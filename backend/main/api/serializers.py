from rest_framework import serializers
from main.models.score import Score

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["id","title","value","created_at"]

        