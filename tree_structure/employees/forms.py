from django import forms
from employees.models import Worker


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['full_name',
                  'position',
                  'employment_date',
                  'salary',
                  'parent'
                  ]
