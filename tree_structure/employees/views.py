from django.core.paginator import Paginator
from django.shortcuts import HttpResponse, HttpResponseRedirect, render

from employees.forms import WorkerForm
from employees.models import Worker


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def show_employees(request):
    if is_ajax(request=request):
        children_id = request.GET['children_id']
        employee = Worker.objects.get(id=children_id)
        employees = employee.get_descendants(include_self="True").\
            filter(level__lte=employee.level + 3)
        response = render(request,
                          'employees_list.html',
                          {'employees': employees}
                          )
        return response
    else:
        employees = Worker.objects.all().filter(level__lte=1)
        return render(request, "employees.html", {'employees': employees})


def show_employees_all(request):
    if request.user.is_authenticated:
        employees = Worker.objects.order_by('date_added')
        current_page = Paginator(list(employees), 20)
        page_number = request.GET.get('page')
        page = current_page.get_page(page_number)
        return render(request, 'employees_all.html', {
            'paginator': current_page,
            'employees': page,
        })
    else:
        return HttpResponseRedirect("/users/login")


def edit(request, employee_id):
    employee = Worker.objects.get(id=employee_id)
    if request.method != 'POST':
        form = WorkerForm(instance=employee, prefix='form')
        request.session['return_path'] = request.META.get('HTTP_REFERER','/')
    else:
        form = WorkerForm(request.POST, instance=employee, prefix='form')
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
        return HttpResponseRedirect(request.session['return_path'])
    context = {'form': form}
    return render(request, 'edit.html', context)


def delete(request, employee_id):
    employee = Worker.objects.get(id=employee_id)
    for child in employee.get_children():
        child.parent = employee.parent
        child.save()
    employee.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def change_boss(request):
    if is_ajax(request=request):
        boss_id = request.GET['boss_id']
        children_id = request.GET['children_id']
        if boss_id == "nestable":
            current_child = Worker.objects.get(id=children_id)
            current_child.move_to(None, 'first-child')
            current_child.save()
        else:
            parent = Worker.objects.get(id=boss_id)
            current_child = Worker.objects.get(id=children_id)
            current_child.move_to(parent, 'first-child')
            current_child.save()
        return HttpResponse('')
