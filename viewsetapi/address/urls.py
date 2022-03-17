from rest_framework.routers import DefaultRouter
from .views import AddressViwSet
from django.urls import path, include

router = DefaultRouter()
router.register('/address',AddressViwSet)

urlpatterns= [
    path ( 'api/', include(router.urls))

]