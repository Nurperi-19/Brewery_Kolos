from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

STATUS_CHOICES = (
    ('Норма', 'Норма'),
    ('Брак', 'Брак'),
    ('Просроченный', 'Просроченный'),
)

class Beer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    identification_number = models.AutoField(primary_key=True, verbose_name='Идентификационный номер')
    unit_of_measure = models.CharField(max_length=10, default="литр", verbose_name='Единица измерения')
    quantity = models.IntegerField(default=1, verbose_name='Количество')
    price = models.IntegerField(blank=False, null=False, verbose_name='Цена')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,  default='Норма')

    def __str__(self):
        return self.name

