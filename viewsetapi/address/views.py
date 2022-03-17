from rest_framework.viewsets import ModelViewSet
from .models import Address
from .serializer import AddessSeriazer

class AddressViwSet (ModelViewSet):
    serializer_class = AddessSeriazer
    queryset = Address.objects.all()
