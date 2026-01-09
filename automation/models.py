from django.db import models
from hashlib import sha256

class Bale_Channel(models.Model):
    channel_username = models.CharField(verbose_name="شناسه کانال",unique=True)
    bot_token = models.CharField(verbose_name="توکن ربات")

    @staticmethod
    def hash_token(bot_token: str) -> str:
        return sha256(bot_token.encode()).hexdigest()

class Eitaa_Channel(models.Model):
    channel_username = models.CharField(verbose_name="شناسه کانال",unique=True)

class Telegram_Channel(models.Model):
    channel_username = models.CharField(verbose_name="شناسه کانال",unique=True)
    bot_token = models.CharField(verbose_name="توکن ربات")
