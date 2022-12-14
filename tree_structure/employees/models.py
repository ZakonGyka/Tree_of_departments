from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Worker(MPTTModel):
    full_name = models.CharField(max_length=200,
                                 unique=True,
                                 verbose_name='ФИО'
                                 )
    position = models.CharField(max_length=200,
                                verbose_name='Должность'
                                )
    employment_date = models.DateTimeField(auto_now_add=False,
                                           verbose_name='Дата найма')
    salary = models.DecimalField(max_digits=15,
                                 decimal_places=2,
                                 verbose_name='Размер заработной платы',
                                 )
    date_added = models.DateTimeField(auto_now_add=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['full_name']

    def __str__(self):
        return f'{self.id}, {self.full_name}, {self.position}'
