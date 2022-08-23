from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_Auctions", views.create, name="create"),
    path("add", views.add, name="add"),
    path("auction/<str:Auctions_Auction_title>", views.auction, name="auction"),
    path("category/<str:Categories_id>", views.category, name="category"),
    path("comment/<int:Auctions_id>", views.comments, name="comments"),
    path("price/<int:Auctions_id>", views.price, name="price"),
    path("add_watchlist/<int:Auctions_id>", views.add_watchlist, name="add_watchlist"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("delete/<int:Auctions_id>", views.close, name="close"),
    path("open-auctions", views.openauctions, name="openauctions"),
    path("closed-auctions", views.closedauctions, name="closedauctions"),

]

