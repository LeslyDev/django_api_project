from english_learning.models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class WordInThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'name']


class ThemeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['id', 'name', 'photo', 'category', 'level']


class ThemeDetailSerializer(serializers.ModelSerializer):
    words = WordInThemeSerializer(required=False, many=True)

    class Meta:
        model = Theme
        fields = '__all__'
