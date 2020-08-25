from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
