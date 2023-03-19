# Web Store by Django

This repo contains source codes for **web store** written by **django** framework based on [mongard](https://www.mongard.ir).

## Main Options
registering users based on phone and verification sms code
see all products, price and descriptions
adding product and category 


## more implemamtation details

in this project we completly have custtemized User admin pannels, for example verification for user is based on  phone number instead of username, and number will be verificated by code that messaged to phone.
if your products are a few, you can load image directly to app.
for loading image in development phase, we add this to urlpattetns in main app:
```
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
dont forget removing it in production phase.


