from django import forms
from .models import *

class CreateAuctionForm(forms.ModelForm):
    class Meta:
        model = Auctions
        fields = ('Auction_title','Auction_category','Auction_description','Auction_price','Auction_image')
        

        labels = {
            'Auction_title': 'title:',
            'Auction_category': 'category:',
            'Auction_description': 'description:',
            'Auction_price': 'price:',
            'Auction_image': 'image:',
        }
    
    def __init__(self, *args, **kwargs):
        super(CreateAuctionForm, self).__init__(*args, **kwargs)
        self.fields['Auction_title'].widget.attrs.update({'class': 'Auction_title'})
        self.fields['Auction_category'].widget.attrs.update({'class': 'Auction_category'})
        self.fields['Auction_description'].widget.attrs.update({'class': 'Auction_description'})
        self.fields['Auction_price'].widget.attrs.update({'class': 'Auction_price'})
        self.fields['Auction_image'].widget.attrs.update({'class': 'Auction_image'})
        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)

        labels = {
            'body': '',
        }

    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({'class': 'comment_body'})
    




class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ('price',)

        labels = {
            'price': '',
        }

    def __init__(self, *args, **kwargs):
        super(PriceForm, self).__init__(*args, **kwargs)
        self.fields['price'].widget.attrs.update({'class': 'price_form','PlaceHolder':'USD'})
    