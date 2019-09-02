from django.contrib import admin
from .models import  TourPack, Client, ClientTour


class TourPackAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "from_to", "start_date", "end_date", "quantity")

# admin.site.register(Article)
admin.site.register(TourPack, TourPackAdmin)
admin.site.register(Client)
admin.site.register(ClientTour)