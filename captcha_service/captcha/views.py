from django.shortcuts import render
from django.http import HttpResponse
import random
import string

from claptcha import Claptcha
from PIL import Image
# Create your views here.

def index(request):
	generateCaptchaImage()
	return render(request, 'captcha/index.html')


def generateRandomCaptcha(n=6):
	char_set  = string.ascii_lowercase + string.ascii_uppercase + '0123456789'
	captcha = (random.choice(char_set) for _ in range(n))
	return ''.join(captcha)
	


def generateCaptchaImage():
	c = Claptcha(generateRandomCaptcha(), 'captcha/FreeMono.ttf',
			resample=Image.BICUBIC, noise=0.3)

	c.write('captcha/static/captcha/captcha.png')


