"""winx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from winxapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
   
    
    path('winxapp/index/', views.index, name='index'),
    path('winxapp/chat/', views.chat, name='chat'),
    path('entertextmsgs/', views.entertextmsgs, name='entertextmsgs'),
    path('entersongmsgs/', views.entersongmsgs, name='entersongmsgs'),
    path('face/', views.face, name='face'),
    path('webcam/', views.webcam, name='webcam'),
    path('song/', views.song, name='song'),
    path('registration/', views.registration, name='registration'),
    path('loginwinx/', views.loginwinx, name='loginwinx'),
    #path('freindlist/', views.freindlist, name='freindlist'),
    path('freindrequest/', views.freindrequest, name='freindrequest'),
    path('sendfrndreq/', views.sendrequest, name='sendrequest'),
    path('freindrequestacc/', views.freindreqacc, name='freindreqacc'),
    path('chatmsgs/', views.chatmsgs, name='chatmsgs'),
    path('music/', views.music, name='music'),
    path('logout/', views.logout, name='logout'),
    path('forgotpassotp/', views.forgotpassotp, name='forgotpassotp'),
    path('confirmotp/', views.confirmotp, name='confirmotp'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('updateprofilefrnd/', views.updateprofilefrnd, name='updateprofilefrnd'),
    path('updateprofileblk/', views.updateprofileblk, name='updateprofileblk'),
    path('storenewpass/', views.storenewpass, name='storenewpass'),
    path('chatcontmsgs/', views.chatcontmsgs, name='chatcontmsgs'),
    path('notcont/', views.contnotify, name='contnotify'),
    path('notblock/', views.notblock, name='notblock'),
    path('sendunblock/', views.sendunblock, name='sendunblock'),
    path('sendblock/', views.sendblock, name='sendblock'),
    path('blockuser/', views.blockuser, name='blockuser'),
    path('deletedata/', views.deletedata, name='deletedata'),
    path('howtouse/', views.howtouse, name='howtouse'),
    path('guide/', views.guide2, name='guide2'),
    path('contactus/', views.contactus, name='contactus'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
