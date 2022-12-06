from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from employees.forms import WorkerForm
from employees.models import Worker


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def show_employees(request):
    if is_ajax(request=request):
        children_id = request.GET['children_id']
        employee = Worker.objects.get(id=children_id)
        employees = employee.get_descendants(include_self="True").filter(level__lte=employee.level + 3)
        response = render(request, 'employees_list.html', {'employees': employees})
        return response
    else:
        employees = Worker.objects.all().filter(level__lte=1)
        return render(request, "employees.html", {'employees': employees})


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


def show_employees_all(request):
    if request.user.is_authenticated:
        if is_ajax(request=request):
            sort_by = request.GET['sort_by']
            search_text = request.GET['q_search']
            employees = Worker.objects.order_by(sort_by).filter(Q(employment_position__icontains=search_text))
            employees = employees | Worker.objects.order_by(sort_by).filter(Q(name__icontains=search_text))
            employees = employees | Worker.objects.order_by(sort_by).filter(Q(salary__icontains=search_text))
            employees = employees | Worker.objects.order_by(sort_by).filter(Q(employment_start_date__icontains=search_text))
            context = {}
            current_page = Paginator(list(employees), 20)
            page_number = request.GET['page']
            page = current_page.get_page(page_number)
            try:
                context['employees'] = page
            except PageNotAnInteger:
                context['employees'] = current_page.page(1)
            except EmptyPage:
                context['employees'] = current_page.page(current_page.num_pages)
            response = render(request, 'employees_all_sort.html', context)
            return response
        else:
            employees = Worker.objects.order_by('date_added')
            context = {}
            current_page = Paginator(list(employees), 20)
            page_number = request.GET.get('page')
            page = current_page.get_page(page_number)
            try:
                context['employees'] = current_page.page(page_number)
            except PageNotAnInteger:
                context['employees'] = current_page.page(1)
            except EmptyPage:
                context['employees'] = current_page.page(current_page.num_pages)
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
