from django.contrib import admin
from .models import Item, OrderItem, Order, Payment, Coupon, Address, Refund

def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'



class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 
                    'ordered', 
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon'
    ]

    search_fields = [
        'user__username',
        'ref-code'
    ]

    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]

    list_filter = ['ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted']

    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'first_name',
        'last_name',
        'username',
        'email',
        'street_address',
        'apartment_address',
        'country',
        'zip_code',
        'address_type',
        'default'
    ]

    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip_code']

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Address, AddressAdmin)
admin.site.register(Refund)