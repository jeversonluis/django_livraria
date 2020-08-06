from django.contrib import admin
from .models import Book, Client, Reservation


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'resume', 'image')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'client_name', 'date_res', 'date_dev')


