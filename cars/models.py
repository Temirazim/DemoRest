from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Car(models.Model):
    vin = models.CharField(max_length=50, verbose_name='Вин', db_index=True, unique=True)
    color = models.CharField(verbose_name='Цвет', max_length=20)
    brand = models.CharField(verbose_name='Бренд', max_length=20)
    CAR_TYPES = (
        (1, 'Седан'),
        (2, 'Хетчбек'),
        (3, 'Уневирсал'),
        (4, 'Купе'),
        (5, 'Джип'),
    )
    car_type = models.IntegerField(verbose_name='Тип машины', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)