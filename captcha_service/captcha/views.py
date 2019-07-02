from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import random
import string

from claptcha import Claptcha
# Create your views here.

def index(request):
	return HttpResponse(generateRandomCaptcha())


def generateRandomCaptcha(n=6):
	char_set  = string.ascii_lowercase + string.ascii_uppercase + '0123456789'
	captcha = (random.choice(char_set) for _ in range(n))

	generateCaptchaImage(''.join(captcha))


def generateCaptchaImage(captcha):
	c = Claptcha(generateRandomCaptcha(), 'FreeMono.ttf',
			resample=Image.BICUBIC, noise=0.3)

	c.write('captcha1.png')


