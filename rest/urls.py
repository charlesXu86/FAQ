"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from rest.Api.QA_server import qa_server
from rest.Api.IM_server import im_server, im_server2

from rest.Api.new_train import train_model
from rest.Api.update_train import train_model_update
from rest.Api.chatbot import bot
from rest.Api.mybot import mybot
from rest.Api.rasa_bot import rasabot

urlpatterns = [
    path('chatbot', qa_server),
    path('imbot', im_server2),
    path('newtrain', train_model),
    path('trainup', train_model_update),
    path('bot', bot),
    path('rbot', mybot),
    path('mybot', rasabot)

]
