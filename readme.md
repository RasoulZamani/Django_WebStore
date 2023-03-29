# Web Store by Django

This repo contains source codes for **web store** written by **django** framework based on [mongard](https://www.mongard.ir).

## Main Options
registering users based on phone and verification sms code,login and logout.
see all categories, products, price and descriptions. by clicking on details you can see more details of each product.
you can add  product and category and sub category. Also in detail page of each product you can order and then see your final cart (contains products,prices and remove button) 
in home page sub categories can seen in dropdown buttons.


## more implemamtation details

in this project we completly have custtemized User admin pannels, for example verification for user is based on  phone number instead of username, and number will be verificated by code that messaged to phone.
if your products are a few, you can load image directly to app.
for loading image in development phase, we add this to urlpattetns in main app:
```
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
dont forget removing it in production phase.

by customizing admin-django command, in account app, we added `remove_expired_otp` for removing expired verification code. pytz pakage is uused for handling timezone (also in setting `TIME_ZONE='Asia/Tehran'`) 

