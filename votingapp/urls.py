from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from.import views
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "E-Voting System Admin"
admin.site.site_title = "E-Voting System Admin Panel"
admin.site.index_title = "Welcome E-Voting System Admin Panel"

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('castvote/', views.castvote, name="castvote"),
    path('systemguide/', views.systemguide, name="systemguide"),
    path('result/', views.result, name="result"),
    path('login1/', views.login1, name="login1"),
    path('registration/', views.registration, name="registration"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('verifyAdhar', views.verifyAdhar, name="verifyAdhar"),
    path('logout/', views.handleLogout, name="handleLogout"),
    path('change_password/<token>/', views.change_password, name="change_password"),
    path('forgot_password', views.forgot_password, name="forgot_password"),
     
]

