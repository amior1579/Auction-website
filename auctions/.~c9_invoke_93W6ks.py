from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render 
from django.urls import reverse
from django.contrib import messages

from .models import *
from .forms import *


def index(request):
    all_auctions = Auctions.objects.all()
    categories_nav = Categories.objects.all()
    return render(request, "auctions/index.html",{
    'all_auctions': all_auctions,
    'categories_nav':categories_nav,    
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



def create(request):
    categories_nav = Categories.objects.all()
    return render(request, 'auctions/Auctions_create.html',{
            'form':CreateAuctionForm,
            'categories_nav':categories_nav
        })



def add(request):
    if request.method == 'POST':
        form = CreateAuctionForm(request.POST, request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.user = request.user
            category = request.POST['Auction_category']
            add.auction_category = category
            add.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        if request.method == 'GET':
            return HttpResponseRedirect(reverse('index'))
        return HttpResponseRedirect(reverse('create'))




def auction(request, Auctions_Auction_title):
    auctions = Auctions.objects.get(Auction_title = Auctions_Auction_title)
    categories_nav = Categories.objects.all()
    price = Price.objects.filter(auction = auctions).last()
    watch = bool
    if auctions.Watchlist.filter(id = request.user.id).exists():
        watch = True
    return render(request, 'auctions/auction.html',{
        'auctions': auctions,
        'comment_form':CommentForm,
        'pricee':price,
        'price_form' : PriceForm,
        'watch':watch,
        'categories_nav':categories_nav
        })
        


def comments(request, Auctions_id):
    auctions = Auctions.objects.get(id = Auctions_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.auctions = auctions
            comment.user = request.user
            comment.save()
        return HttpResponseRedirect(reverse('auction' , args=(auctions.Auction_title,)))
    return render(request, 'auctions/index.html',)
   

def price(request, Auctions_id):
    auctions = Auctions.objects.get(id = Auctions_id)
    auction_price = auctions.Auction_price
    last_price = Price.objects.filter(auction = auctions).last()
    if request.method == 'POST':
        form = PriceForm(request.POST)
        if form.is_valid():
                form_save = form.save(commit=False)
                form_save.auction = auctions
                form_save.user = request.user
                formss = form_save.price
                if last_price is not None:
                    last = last_price.price
                    if last < formss:
                        form_save.save()
                        return HttpResponseRedirect(reverse('auction' , args=(auctions.Auction_title,)))
                    else:
                        messages.add_message(request, messages.WARNING, 'Your bid price is lower than the last bid price')
                        return HttpResponseRedirect(reverse('auction' , args=(auctions.Auction_title,)))

                elif auction_price < formss:
                    form_save.save()
                    return HttpResponseRedirect(reverse('auction' , args=(auctions.Auction_title,)))

                else:
                    messages.add_message(request, messages.WARNING, 'Your bid price is lower than the last bid price')
                    return HttpResponseRedirect(reverse('auction' , args=(auctions.Auction_title,)))


                     
    



def category(request, Categories_id):
    category = Categories.objects.get(id = Categories_id)
    auctions = Auctions.objects.filter(Auction_category = category)
    categories_nav = Categories.objects.all()
    return render(request, 'auctions/categories.html',{
            'auction':auctions,
            'category':category,
            'categories_nav':categories_nav
        })




def add_watchlist(request, Auctions_id):
    auctions = Auctions.objects.get(id = Auctions_id)
    if auctions.Watchlist.filter(id = request.user.id).exists():
        auctions.Watchlist.remove(request.user)
    else:
        auctions.Watchlist.add(request.user)
    return HttpResponseRedirect(reverse('auction', args=(auctions.Auction_title,)))


def watchlist(request,):
    watchlist = Auctions.objects.filter(Watchlist=request.user)
    categories_nav = Categories.objects.all()
    return render(request, 'auctions/watchlist.html',{
            'all_watchlist':watchlist,
            'categories_nav':categories_nav
        })



def close(request, Auctions_id):
    auctions = Auctions.objects.get(id = Auctions_id)
    if auctions.user == request.user:
        auctions.active = False
        auctions.buyer = Price.objects.filter(auction=auctions).last().user
        auctions.save()
        return HttpResponseRedirect(reverse('auction', args=(auctions.Auction_title,)))
    else:
        return HttpResponseRedirect(reverse('index'))