from django.contrib import admin
from .models import *

class AuctionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Auction_title', 'Auction_category', 'Auction_price','buyer')
    
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'auctions', 'date_added')

class PriceAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'auction')

admin.site.register(User)
admin.site.register(Auctions,AuctionsAdmin)
admin.site.register(Categories)
admin.site.register(Comments,CommentsAdmin)
admin.site.register(Price,PriceAdmin)

