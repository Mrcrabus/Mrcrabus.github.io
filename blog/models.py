from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(upload_to='news_img', default='def_bg.jpg')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def save(self, **kwargs):
        super().save()

        image = Image.open(self.img.path)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})


class Book(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    img = models.ImageField(upload_to='books_img', default='def_bg.jpg')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        super().save()

        image = Image.open(self.img.path)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})


class Evolution(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    img = models.ImageField(upload_to='evo_img', default='def_bg.jpg')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        super().save()

        image = Image.open(self.img.path)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})
