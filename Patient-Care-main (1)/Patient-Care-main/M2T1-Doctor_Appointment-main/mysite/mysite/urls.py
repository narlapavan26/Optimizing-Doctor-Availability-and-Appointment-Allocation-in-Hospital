
from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path ('login/',views.login),
    path('book/',views.book),
    path('signup/',views.signup)
]
