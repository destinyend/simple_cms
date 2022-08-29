from main.db_generate.generators import UserGenerator, Field
from main.models import User


def user_generate() -> [User]:
    """Генерирует возможных пользователей"""
    fields = [
        Field('status', [User.StatusChoice.BANNED, User.StatusChoice.ACTIVE]),
        Field('auto_translate', [True, False]),
        Field('auto_sound', [True, False]),
    ]
    generator = UserGenerator(User, fields)
    users = generator.generate()
    print('Users created')
    return users


def db_generate():
    """Создает тестовую ДБ, комбинируя возможные варианты. Будет создано около 20к различных объектов"""
    users = user_generate()
