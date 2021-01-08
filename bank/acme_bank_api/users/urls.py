from django.conf.urls import url, include
from rest_framework.authtoken import views as auth_view
from acme_bank_api.users import views
from django.contrib.auth.models import User
#from rest_framework import

urlpatterns = [
    url(r'signup/', views.UserCreate.as_view(), name='user-create'),
    url(r'^signin/', auth_view.obtain_auth_token, name='account_login'),
    url(r'^api-token-auth/',auth_view.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]