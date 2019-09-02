from django.contrib import admin
from .models import  TourPack, Client, ClientTour, ClientTourParticipant, Order


class TourPackAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "from_where", "to", "start_date", "end_date", "quantity")

class ClientAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "phone_number", "password_id", "created_at")

class ClientTourAdmin(admin.ModelAdmin):
    list_display = ("tourpack_id", "client_id", "adult_count", "child_count", "created_at")

class ClientTourParticipantAdmin(admin.ModelAdmin):
    list_display = ("clietntour_id", "client_id", "created_at")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("clietntour_id", "status", "payment_status", "payment_methods" "created_at")



# admin.site.register(Article)
admin.site.register(TourPack, TourPackAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ClientTour, ClientTourAdmin)
admin.site.register(ClientTourParticipant, ClientTourParticipantAdmin)
admin.site.register(Order, OrderAdmin)