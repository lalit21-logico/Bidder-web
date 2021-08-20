from django.contrib import admin
from BidderWeb.models import BWUser
from BidderWeb.models import *

# Register your models here.
admin.site.register(BWUser)
admin.site.register(product_data)
admin.site.register(watchlist_data)
admin.site.register(cart_data)
admin.site.register(schedular_flag)
