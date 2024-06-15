from django.contrib import admin
from .models import Clients, Subscriptions
from .forms import ClientsForm


admin.site.empty_value_display = 'Не задано'


class SubscriptionsInline(admin.StackedInline):
    model = Subscriptions
    extra = 0


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    form = ClientsForm
    list_display = (
        'name',
        'external_id',
        'date_added'       
    )
    inlines = (
        SubscriptionsInline,
    )


@admin.register(Subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'start_date',
        'amount_of_days',
        'product',
        'current_status',
        'expire_date'
    )
    list_editable = (
        'amount_of_days',
        'product',
        'current_status',
    )    
    search_fields = ('client', 'product') 
    list_filter = ('client', 'product',)
    list_display_links = ('client',)
