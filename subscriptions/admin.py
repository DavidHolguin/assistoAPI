from django.contrib import admin
from subscriptions.models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'is_active')
    search_fields = ('user__username', 'user__email')
    list_filter = ('is_active',)
