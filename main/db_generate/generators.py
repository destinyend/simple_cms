from copy import deepcopy
from random import randint

class Field:
    """Описание поля для генерации моделей name - имя поля, diapason - возможные варианты"""

    def __init__(self, name: str, diapason: []):
        self.name = name
        self.diapason = diapason


class ModelGenerator:
    def __init__(self, model, fields: [Field]):
        self.variants = None
        self.model = model
        self.fields = fields

    def combine(self, fields: [Field], instances: [] = None) -> [{}]:
        """Комбинирует параметры, возвращает все возможные комбинации переданных полей"""
        if not fields:  # крайний случай рекурсии
            self.variants = instances
            return
        field = fields.pop()  # выкидываем поле из массива
        extended = []  # здесь будем сохранять расширенные экземпляры

        if not instances:  # инициализируем вариантами из первого диапазона значений
            for variant in field.diapason:
                extended.append({field.name: variant})
        else:  # комбинируем с существующими экземплярами
            for variant in field.diapason:
                for instance in deepcopy(instances):
                    instance[field.name] = variant
                    extended.append(instance)
        return self.combine(fields, extended)

    def create_objects(self):
        """Создаёт объекты используя варианты сгенерированные self.combine"""
        return [
            self.model.objects.create(**fields)
            for fields in self.variants
        ]

    def generate(self):
        """Запускает полный цикл генерации объектов и возвращает их"""
        self.combine(self.fields)
        return self.create_objects()


class UserGenerator(ModelGenerator):
    def create_objects(self):
        return [
            self.model.objects.create(username=f'user{n}@.domain.ru', **variant)
            for n, variant in enumerate(self.variants)
        ]


SYMBOLS = """ fFыЫ!"№;%:?*()ХЪ'"<>/?`ё№$-+={}[],.^\\|"""  # набор символов для генерации текстовых полей


def generate_text(symbol: str) -> str:
    """Генерирует текстовое поле случайной длины с обязательным символом"""
    text = []
    for _ in range(randint(3, 50)):
        index = randint(0, len(SYMBOLS) - 1)
        text.append(SYMBOLS[index])
    index = randint(0, len(text) - 1)
    text[index] = symbol
    return ''.join(text)



