#Captcha Service API

##Overview
This is simple captcha REST API built using Python, Django, DRF (Django Rest Framework). 
I have used JWT authentication for authenticating the user. Once the user is authenticated you receive a token, with which you can request a captcha. One can easily plug this API in their code.

##Usage
Download/ Clone the code and access the API using below Urls.
1. POST /api/token/
{
username: admin
password: password11
}
The above request will return 2 tokens as below:

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjQ0MDAxMDQsInRva2VuX3R5cGUiOiJyZWZyZXNoIiwidXNlcl9pZCI6MSwianRpIjoiYjEwZDU1MTUxYWRkNGFjYmE2NTdiNGFjM2JlMzliYmIifQ.pDygt-N3yAh6Yo2HReHUdhYUrefRtBgFh1yrAzLZubg",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjQzMTQwMDQsInRva2VuX3R5cGUiOiJhY2Nlc3MiLCJ1c2VyX2lkIjoxLCJqdGkiOiJhZjU3ZmJkY2NjMWI0MjRiYjhiZDc2Mjk5YzUxZjZkNyJ9.yR35XxL47UogEOj0Aze-4cp4zH_Px2W9WycbVl28cJs"
}

2. GET /api/
   Pass the access token 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjQzMTQwMDQsInRva2VuX3R5cGUiOiJhY2Nlc3MiLCJ1c2VyX2lkIjoxLCJqdGkiOiJhZjU3ZmJkY2NjMWI0MjRiYjhiZDc2Mjk5YzUxZjZkNyJ9.yR35XxL47UogEOj0Aze-4cp4zH_Px2W9WycbVl28cJs' as the bearer token in the header. This is will return a captcha Image.
   
3. GET /api/captcha/CAPTCHA_TEXT with Bearer as the access token
   where CAPTCHA_TEXT is the text entered by user. If the user enters correct text, then the status will be returned as True else False
   {"status": true}
   
4. POST /api/token/refresh
{
 refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjQ0MDAxMDQsInRva2VuX3R5cGUiOiJyZWZyZXNoIiwidXNlcl9pZCI6MSwianRpIjoiYjEwZDU1MTUxYWRkNGFjYmE2NTdiNGFjM2JlMzliYmIifQ.pDygt-N3yAh6Yo2HReHUdhYUrefRtBgFh1yrAzLZubg"
}
   If the access token expires you can request a new token using the above request. 
   Pass the refresh token in the body. This is return a new access token to access the captcha.
   
   




