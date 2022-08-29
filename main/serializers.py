from rest_framework.serializers import ModelSerializer
from main.models import *


def create_model_serializer(model_name: str) -> type:
    """Метакласс создающий сериалайзеры по имени модели"""
    meta = type('Meta', (object,), {'fields': '__all__', 'model': globals()[model_name]})
    args = {'Meta': meta}
    return type(f'{model_name}Serializer', (ModelSerializer,), args)


class UserSerializer(create_model_serializer('User')):
    class Meta:
        model = User
        fields = ('id',)


BlockSerializer = create_model_serializer('Block')

