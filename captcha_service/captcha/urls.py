from django.urls import path

from . import views

urlpatterns = [
	path('', views.returnCaptcha, name='captcha')
]