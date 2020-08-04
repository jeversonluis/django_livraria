from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Base(models.Model):
    creation = models.DateField('Creation', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)

    class Meta:
        abstract = True


class Book(Base):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=100, blank=False, null=False)
    author = models.CharField('Author', max_length=100, blank=False, null=False)
    resume = models.TextField()
    available = models.BooleanField(default=True, verbose_name='Available')
    image = models.ImageField(upload_to='static/images')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title


class Client(Base):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=100, blank=False, null=False)
    last_name = models.CharField('Last Name', max_length=100, blank=False, null=False)
    email = models.EmailField()
    phone = models.CharField('Phone', max_length=12, blank=False, null=False)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name

