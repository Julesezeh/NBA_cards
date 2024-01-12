from rest_framework import serializers



class CardSerializer(serializers.Serializer):
    player = serializers.CharField
    team = serializers.CharField()
    three_pt = serializers.FloatField()
    ppg = serializers.FloatField()
    rpg = serializers.FloatField()
    apg = serializers.FloatField()
    stpg = serializers.FloatField()