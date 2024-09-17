from django.contrib import admin
from users.models import CustomUser  # Usamos CustomUser en lugar de User
from subscriptions.models import Subscription  # Asume que tienes un modelo Subscription en la app subscriptions

@admin.register(CustomUser)  # Registramos CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'is_active')  # Eliminamos 'plan' ya que no existe
    search_fields = ('user__username', 'user__email')
    list_filter = ('is_active',)
