from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('book', views.BookView)
router.register('customer', views.CustomerView)
router.register('loan', views.LoanView)

urlpatterns = [
    path('', include(router.urls)),

]
