from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from .views import *

router = routers.DefaultRouter()
router.register('min', min_view_set, basename='min')
router.register('max', max_view_set, basename='max')
router.register('wallet', wallet_view_set, basename='wallet')
router.register('transaction', transaction_view_set, basename='transaction')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

