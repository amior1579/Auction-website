from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.username}'
    


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.tag}'



class Auctions(models.Model):
    id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='create_user')
    Auction_title = models.CharField(max_length=50)
    Auction_category = models.ForeignKey(Categories,on_delete=models.CASCADE, null=True)
    Auction_description = models.TextField(max_length=500, blank=True)
    Auction_price = models.FloatField(null=True)
    Auction_image = models.ImageField(null=True, blank=True, upload_to="images/")
    Watchlist = models.ManyToManyField(User,blank=True,default=None, related_name='auction_watchlist')
    buyer = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)
    bid_price = models.FloatField( null=True, blank=True)

    def __str__(self):
        return f' {self.id},{self.Auction_title},{self.Auction_category.tag}'



class Price(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    auction = models.ForeignKey(Auctions, on_delete=models.CASCADE ,null=True)
    
    def __str__(self):
        return f'{self.id}, {self.price},{self.user},{self.auction}'



class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    auctions = models.ForeignKey(Auctions, on_delete=models.CASCADE, related_name='comments', null=True)
    body = models.TextField()

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'Comment {self.body} by {self.user}'






