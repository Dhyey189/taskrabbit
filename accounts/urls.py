from django.contrib import admin
from django.urls import path
from accounts.views import signup, home, login_view, logout, profile

urlpatterns = [
    path('signup/', signup),
    path('login/', login_view),
    path('home/', home),
    path('logout/', logout),
    path('profile/', profile)
]