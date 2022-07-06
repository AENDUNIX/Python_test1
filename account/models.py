from django.contrib.auth.models import User
from django.db import models

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    name = models.CharField(max_length=15, verbose_name="Имя")
    user_name = models.CharField(max_length=11, verbose_name="Юзернейм")
    user_telegram_id = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='Юзер-айди')
