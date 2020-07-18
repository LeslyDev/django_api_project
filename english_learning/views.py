from django.shortcuts import render
from english_learning.models import *
from english_learning.serializers import *
from rest_framework import generics
from .permissions import Check_API_KEY_Auth


class CategoryList(generics.ListAPIView):
    # permission_classes = (Check_API_KEY_Auth,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LevelList(generics.ListAPIView):
    # permission_classes = (Check_API_KEY_Auth,)
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ThemeList(generics.ListAPIView):
    # permission_classes = (Check_API_KEY_Auth,)
    queryset = Theme.objects.all()
    serializer_class = ThemeListSerializer


class ThemeDetail(generics.RetrieveAPIView):
    # permission_classes = (Check_API_KEY_Auth,)
    queryset = Theme.objects.all()
    serializer_class = ThemeDetailSerializer


class WordDetail(generics.RetrieveAPIView):
    # permission_classes = (Check_API_KEY_Auth,)
    queryset = Word.objects.all()
    serializer_class = WordSerializer
