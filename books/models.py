from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    creation = models.DateField('Creation', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)

    class Meta:
        abstract = True


class Book(Base):
    title = models.CharField('Title', max_length=100, blank=False, null=False)
    author = models.CharField('Author', max_length=100, blank=False, null=False)
    resume = models.TextField()
    status = models.BooleanField(default=True, verbose_name='Status')
    image = StdImageField(upload_to='static/img', variations={'thumb': {'width': 200, 'height': 200, 'crop': True}})

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title


class Client(Base):
    name = models.CharField('Name', max_length=100, blank=False, null=False)
    email = models.EmailField()
    phone = models.CharField('Phone', max_length=12, blank=False, null=False)
    cpf = models.CharField('CPF', max_length=10, blank=False, null=False)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name


class Reservation(Base):
    date_res = models.DateField()
    date_dev = models.DateField()
    book_name = models.ForeignKey(Book, verbose_name='Book', on_delete=models.CASCADE)
    client_name = models.ForeignKey(Client, verbose_name='Client', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'


