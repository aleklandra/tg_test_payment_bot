from django.contrib import admin
from .models import Clients, Subscriptions


admin.site.empty_value_display = 'Не задано'

class SubscriptionsInline(admin.StackedInline):
    model = Subscriptions
    extra = 0


class ClientsAdmin(admin.ModelAdmin):
    inlines = (
        SubscriptionsInline,
    )
    list_display = (
        'name',
        'external_id',
        'date_added'        
    )

class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'start_date',
        'amount_of_days',
        'product',
        'current_status',
    )
    list_editable = (
        'amount_of_days',
        'product',
        'current_status',
    )    
    search_fields = ('client', 'product') 
    list_filter = ('client', 'product',)
    list_display_links = ('client',)


admin.site.register(Clients, ClientsAdmin)
admin.site.register(Subscriptions, SubscriptionsAdmin)
