from rest_framework import serializers
from .models import Proyecto

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('id','titulo', 'descripcion', 'tecnologias','creado_en')
        rear_only_fields = ('creado_en',)
