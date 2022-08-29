import os

from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from main.tasks import send_code_email
from main.permissions import *
from main.serializers import *
from main.validators import UsernameValidator
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


class BlocksView(create_view('Block')):
    @action(['PATCH'], detail=True, permission_classes=(IsActiveUser,))
    def bg_image(self, request, pk):
        block = Block.objects.get(pk=pk)
        if block.bg_image:
            os.remove(block.bg_image.path)
        block.bg_image = request.data['file']
        block.save()
        return Response({'file': block.bg_image.url}, status=status.HTTP_200_OK)

# class ImagesView(create_view('Image')):
#     def create(self, request):
#         image = Image.objects.create(file=request.data['file'])
#         return Response(
#             ImageSerializer(image).data,
#             status=status.HTTP_201_CREATED
#         )

#
# FontsView = create_view('Font')
# TitlesView = create_view('Text')
# BlockTemplatesView = create_view('BlockTemplate')
# TextTemplatesView = create_view('TextTemplate')
