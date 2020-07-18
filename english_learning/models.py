from django.db import models
from django.conf import settings
# from audiofield.fields import AudioField
import os.path


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='categories/', null=True, blank=True)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Word(models.Model):
    name = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    transcription = models.CharField(max_length=255)
    example = models.CharField(max_length=255)
    sound = models.SlugField(unique=True)
    # audio_file = AudioField(upload_to='sounds/', blank=True,
    #                         ext_whitelist=(".mp3", ".wav", ".ogg"),
    #                         help_text=("Allowed type - .mp3, .wav, .ogg"))
    #
    # # Add this method to your model
    # def audio_file_player(self):
    #     """audio player tag for admin"""
    #     if self.audio_file:
    #         file_url = settings.MEDIA_URL + str(self.audio_file)
    #         player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (
    #             file_url)
    #         return player_string
    #
    # audio_file_player.allow_tags = True
    # audio_file_player.short_description = ('Audio file player')

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=100)
    photo = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,
                                 related_name='theme_category')
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING,
                              related_name='theme_level')
    words = models.ManyToManyField(Word, related_name='theme_words')

    def __str__(self):
        return self.name
