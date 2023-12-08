from django.db import models
from django.contrib.auth.models import User


class Chats(models.Model):
    owner1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='own1')
    owner2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='own2')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "чат"
        verbose_name_plural = "чати"


class Messages(models.Model):
    chat = models.ForeignKey(Chats, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    class Meta:
        verbose_name = "повідомлення"
        verbose_name_plural = "повідомлення"
