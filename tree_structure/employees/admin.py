from django.contrib import admin
from employees.models import Worker

# from . import random_employee


@admin.register(Worker)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'position',
        'employment_date',
        'salary',
        'parent',
        'date_added'
    )
    list_filter = ('position',)
    list_display_links = ('full_name',)
    search_fields = ('full_name',
                     'employment_date',
                     'salary',
                     )
    empty_value_display = '-отсутствует-'


# admin.site.register(Worker, EmployeesAdmin)
