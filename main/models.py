from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import *


class UserManager(BaseUserManager):
    def create_user(self, username, **kwargs) -> 'User':
        user = self.model(username=username, **kwargs)
        if 'password' in kwargs:
            user.set_password(kwargs['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None) -> 'User':
        user = self.create_user(username, password=password, is_staff=True, is_superuser=True)
        return user

    def create_staffuser(self, username, ) -> 'User':
        return self.create_user(username, is_staff=True)


class User(AbstractUser):
    class StatusChoice(TextChoices):
        ACTIVE = 'a'
        BANNED = 'b'

    objects = UserManager()
    username = CharField(max_length=64, db_index=True, unique=True)
    email = None
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    status = CharField(max_length=1, default=StatusChoice.ACTIVE, choices=StatusChoice.choices)

    class Meta:
        db_table = 'users'


class ApiStat(Model):
    """Класс для сбора статистики по запросам в мидлваре"""

    class Meta:
        db_table = 'api_stat'

    request = CharField(max_length=128)
    time = FloatField()


class Block(Model):
    class Meta:
        ordering = ('number',)
        db_table = 'blocks'

    class PositionChoices(TextChoices):
        TOP = 'top'
        BOTTOM = 'bottom'
        LEFT = 'left'
        RIGHT = 'right'

    class DirectionChoices(TextChoices):
        HORIZONTAL = 'horizontal'
        VERTICAL = 'vertical'

    number = SmallIntegerField(default=999)
    html = TextField(default='', blank=True)
    background = CharField(max_length=16, blank=True, default='')
    bg_image = FileField(upload_to='images', blank=True)
    height= PositiveSmallIntegerField(default=100)
    #  параметры эффектов
    direction = CharField(max_length=10, default=DirectionChoices.HORIZONTAL, choices=DirectionChoices.choices)
    position = CharField(max_length=6, default=PositionChoices.TOP, choices=PositionChoices.choices)
    speed = PositiveSmallIntegerField(default=10)

