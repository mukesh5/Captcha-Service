from claptcha import Claptcha
from django.shortcuts import render
from django.http import HttpResponse
import json
from PIL import Image
import random
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
import string

from . import serializers


# Create your views here.

# def index(request):
# 	generateCaptchaImage()
# 	return render(request, 'captcha/index.html')

CAPTCHA_TEXT = ''
def generateRandomCaptcha(n=6):
	char_set  = string.ascii_lowercase + string.ascii_uppercase + '0123456789'
	captcha = (random.choice(char_set) for _ in range(n))
	return ''.join(captcha)
	


def generateCaptchaImage():
	global CAPTCHA_TEXT
	c = Claptcha(generateRandomCaptcha(), 'captcha/FreeMono.ttf',
			resample=Image.BICUBIC, noise=0.3)

	CAPTCHA_TEXT, _ = c.write('captcha/static/captcha/captcha.png')

	return CAPTCHA_TEXT 



@api_view()
@permission_classes([IsAuthenticated])
def returnCaptcha(request):
	print(request.META['USERNAME'])
	text = generateCaptchaImage()
	#print(text)	
	with open('captcha/static/captcha/captcha.png', 'rb') as f:
		return HttpResponse(f.read(), content_type='image/png')

		
@api_view()
def matchCaptchaText(request, text):
	global CAPTCHA_TEXT
	#print(text, CAPTCHA_TEXT)
	if text==CAPTCHA_TEXT:
		CAPTCHA_TEXT = ''
		status = {'status':True}
		return HttpResponse(json.dumps(status))
	else:
		status = {'status':False}
		return HttpResponse(json.dumps(status))