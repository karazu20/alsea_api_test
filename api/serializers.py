from rest_framework import serializers
from api.models import *


class AbrahammrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abrahammr
        fields = ('nombre', 'apellido', 'comentarios', 'creacion', 'actualizacion' )
