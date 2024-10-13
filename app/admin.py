from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Item
from core.models import CustomUser
# Register your models here.

admin.site.register(Item)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_credits', 'date_joined', 'last_login', 'number_of_items_per_user')

    def number_of_items_per_user(self, obj):
        count = Item.objects.filter(user=obj).count()
        
        url = (
            reverse('admin:app_item_changelist')#Assuming the app after admin: is called 'app'
            + f'?user__id__exact={obj.id}'
        )
        return format_html('<a href="{}">{}</a>', url, count)
        
        #return count

    number_of_items_per_user.short_description = 'Number of Items'
