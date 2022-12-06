from django.urls import path

from employees import views

urlpatterns = [
    path('', views.show_employees, name='show_employees'),
    path('employees/', views.show_employees, name='show_employees'),
    path('change_boss/', views.change_boss, name='change_boss'),
    path('employees_all/', views.show_employees_all, name='show_employees_all'),
    path('edit/<employee_id>/', views.edit, name='edit'),
    path('delete/<employee_id>/', views.delete, name='delete'),
]
