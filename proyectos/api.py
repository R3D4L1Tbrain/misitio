from .models import Proyecto
from .serializers import ProyectoSerializer
from rest_framework import viewsets, permissions

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset= Proyecto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProyectoSerializer