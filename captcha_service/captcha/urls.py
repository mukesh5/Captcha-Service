from django.urls import path

from . import views

urlpatterns = [
	path('', views.returnCaptcha, name='captcha'),
	path('captcha/<str:text>', views.matchCaptchaText, name='matchCaptcha')
]