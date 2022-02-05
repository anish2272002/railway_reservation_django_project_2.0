from django.urls import path

from .views import *

email_link_path='claim-account-confirmation-token-ff9dcccf380287f026b3ecc819643'
urlpatterns=[
    path('', login),
    path('sign', sign),
    path('confirmation', confirmation),
    path('dash', dash),
    path(email_link_path, confirmed),
]
