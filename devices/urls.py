from django.urls import path
from .views import (
    CreateAuthTokenView,
)

app_name = 'devices'
urlpatterns = [
    path('api/v1/token/create', CreateAuthTokenView.as_view(), name='create-auth-token')
]