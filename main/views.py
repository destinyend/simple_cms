import os
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from main.tasks import send_email
from main.permissions import *
from main.serializers import *
from rest_framework.mixins import *


def create_view(model_name):
    """Метакласс для создания простых представлений"""

    serializer_class = globals()[f'{model_name}Serializer']
    queryset = globals()[model_name].objects.all()
    return type(
        f'{model_name}sView',
        (ModelViewSet,),
        {'queryset': queryset, 'serializer_class': serializer_class, 'permission_classes': (AllowAny,)}
    )


class UsersView(GenericViewSet, UpdateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.exclude(status=User.StatusChoice.BANNED)

    @action(['GET'], detail=False)
    def self(self, request):
        """Получение информации о текущем пользователе"""
        return Response(
            UserSerializer(request.user).data,
            status=status.HTTP_200_OK
        )

    @action(['POST'], detail=False, permission_classes=(AllowAny,))
    def send_email(self, request):
        send_email.delay(request.data['email'], request.data['message'])
        return Response(status=status.HTTP_200_OK)


class BlocksView(create_view('Block')):
    @action(['PATCH'], detail=True, permission_classes=(IsActiveUser,))
    def bg_image(self, request, pk):
        """Удаление существующего изображения, загрузка нового"""
        block = Block.objects.get(pk=pk)
        if block.bg_image:
            os.remove(block.bg_image.path)
        block.bg_image = request.data['file']
        block.save()
        return Response({'file': block.bg_image.url}, status=status.HTTP_200_OK)


#  создание админа для тестов
try:
    try:
        User.objects.get(id=1)
    except:
        user = User.objects.create(username='admin')
        user.set_password('admin')
        user.save()
except:
    pass
