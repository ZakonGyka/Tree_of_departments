import random

from django.core.files import File

from employees.forms import WorkerForm
from employees.models import Worker

first_name = "Jay", "Jim", "Roy", "Axel", "Billy", "Charlie", "Jax", "Gina",\
             "Paul","Ringo", "Ally", "Nicky", "Cam", "Ari", "Trudie", "Cal",\
             "Carl", "Lady", "Lauren", "Ichabod", "Arthur", "Ashley", "Drake",\
             "Kim", "Julio", "Lorraine", "Floyd", "Janet","Lydia", "Charles",\
             "Pedro", "Bradley", "Aaron", "Abraham", "Adam", "Adrian",\
             "Aidan", "Alan", "Albert", "Alejandro", "Alex", "Alexander",\
             "Alfred", "Andrew", "Angel", "Anthony", "Antonio", "Ashton",\
             "Austin", "Daniel", "David", "Dennis", "Devin", "Diego",\
             "Dominic", "Donald", "Douglas", "Dylan", "Harold", "Harry",\
             "Hayden", "Henry", "Herbert", "Horace", "Howard", "Hugh",\
             "Hunter", "Malcolm", "Martin", "Mason", "Matthew", "Michael",\
             "Miguel", "Miles", "Morgan"


last_name = "Barker", "Style", "Spirits", "Murphy", "Blacker", "Bleacher",\
            "Rogers", "Warren", "Keller", "Smith", "Johnson", "Williams",\
            "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez",\
            "Wilson", "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez",\
            "Moore", "Martin", "Jackson", "Thompson", "White", "Lopez", "Lee",\
            "Gonzalez", "Harris", "Clark", "Lewis", "Robinson", "Walker",\
            "Perez", "Hall", "Young", "Allen", "Sanchez", "Wright", "King",\
            "Scott", "Green", "Baker", "Adams", "Nelson", "Hill", "Ramirez",\
            "Campbell", "Mitchell", "Roberts", "Carter", "Phillips", "Evans",\
            "Turner", "Torres", "Parker", "Collins", "Edwards", "Stewart",\
            "Flores", "Morris", "Nguyen", "Murphy", "Rivera", "Cook",\
            "Rogers", "Morgan", "Peterson", "Cooper", "Reed", "Bailey",\
            "Bell", "Gomez", "Kelly", "Howard", "Ward", "Cox", "Diaz",\
            "Richardson", "Wood", "Watson", "Brooks", "Bennett", "Gray",\
            "James", "Reyes", "Cruz", "Hughes", "Price", "Myers", "Long",\
            "Foster", "Sanders", "Ross", "Morales", "Powell", "Sullivan",\
            "Russell", "Ortiz", "Jenkins", "Gutierrez", "Perry", "Butler",\
            "Barnes", "Fisher", "Henderson", "Coleman", "Simmons", "Jordan",\
            "Patterson", "Reynolds", "Hamilton", "Graham", "Kim", "Gonzales",\
            "Alexander", "Ramos", "Wallace", "Griffin", "West", "Cole",\
            "Hayes", "Chavez",  "Gibson", "Bryant", "Ellis", "Stevens",\
            "Murray", "Ford", "Marshall", "Owens", "McDonald", "Harrison",\
            "Ruiz", "Kennedy", "Wells", "Alvarez", "Woods", "Mendoza",\
            "Castillo", "Olson", "Webb", "Washington", "Tucker", "Freeman",\
            "Burns", "Henry", "Vasquez", "Snyder", "Simpson", "Crawford",\
            "Jimenez", "Porter", "Mason", "Shaw", "Gordon", "Wagner",\
            "Hunter", "Romero", "Hicks", "Dixon", "Hunt", "Palmer",\
            "Robertson", "Black", "Holmes", "Stone", "Meyer", "Boyd",\
            "Mills", "Warren", "Fox", "Rose", "Rice", "Moreno", "Schmidt",\
            "Patel", "Ferguson", "Nichols", "Herrera", "Medina", "Ryan",\
            "Fernandez", "Weaver", "Daniels", "Stephens", "Gardner", "Payne",\
            "Kelley", "Dunn", "Pierce", "Arnold", "Tran", "Spencer", "Peters",\
            "Hawkins", "Grant", "Hansen", "Castro", "Hoffman", "Hart",\
            "Elliott", "Cunningham", "Knight", "Bradley"


def random_generator():
    full_name = random.choice(first_name) + ' ' + random.choice(last_name)
    employee_day = str(random.choice(range(1, 31)))
    employee_month = str(random.choice(range(1, 13)))
    employee_year = str(random.choice(range(2010, 2022)))
    employment_date = employee_year + '-' + employee_month + '-' + employee_day
    salary_level_1 = random.choice(range(5000, 6000, 100))
    salary_level_2 = random.choice(range(4000, 5000, 100))
    salary_level_3 = random.choice(range(3000, 4000, 100))
    salary_level_4 = random.choice(range(2000, 3000, 100))
    salary_level_5 = random.choice(range(1000, 2000, 100))
    return full_name, employment_date, salary_level_1, salary_level_2,\
           salary_level_3, salary_level_4, salary_level_5


def run_random():
    count_one = 0
    for i_one in range(5):
        count_one = count_one + 1
        full_name, employment_date, salary_level_1, salary_level_2, \
        salary_level_3, salary_level_4, salary_level_5 = random_generator()
        form = WorkerForm(data={'full_name': full_name,
                                'position': "level 1",
                                'employment_date': employment_date,
                                'salary': salary_level_1})
        form.save()
        current_child_len = Worker.objects.order_by('date_added')
        current_child_id = current_child_len[(len(current_child_len) - 1)]
        boss_level_1_id = current_child_id.id
        boss_level_1 = Worker.objects.get(id=current_child_id.id)
        boss_level_1.move_to(None, 'left')
        boss_level_1.save()

        count_two = 0
        for i_two in range(3):
            count_two = count_two + 1
            full_name, employment_date, salary_level_1, salary_level_2, \
            salary_level_3, salary_level_4, salary_level_5 = random_generator()
            try:
                form = WorkerForm(data={'full_name': full_name,
                                        'position': "level 2",
                                        'employment_date': employment_date,
                                        'salary': salary_level_2
                                        }
                                  )
                form.save()
                current_child_len = Worker.objects.order_by('date_added')
                current_child_id = current_child_len[(len(current_child_len) - 1)]
                boss_level_2_id = current_child_id.id
                boss_level_2 = Worker.objects.get(id=current_child_id.id)
                boss_level_1 = Worker.objects.get(id=boss_level_1_id)
                boss_level_2.move_to(boss_level_1, 'first-child')
                boss_level_2.save()
            except Exception as inst:
                print('WARNING 2 !!!')
                print(type(inst))
                print(inst.args)

            count_three = 0
            for i_three in range(3):
                count_three = count_three + 1
                full_name, employment_date, salary_level_1, salary_level_2, \
                salary_level_3, salary_level_4, salary_level_5 = random_generator()
                try:
                    form = WorkerForm(data={'full_name': full_name,
                                            'position': "level 3",
                                            'employment_date': employment_date,
                                            'salary': salary_level_3
                                            }
                                      )
                    form.save()
                    current_child_len = Worker.objects.order_by('date_added')
                    current_child_id = current_child_len[(len(current_child_len) - 1)]
                    boss_level_3_id = current_child_id.id
                    boss_level_3 = Worker.objects.get(id=current_child_id.id)
                    boss_level_2 = Worker.objects.get(id=boss_level_2_id)
                    boss_level_3.move_to(boss_level_2, 'first-child')
                    boss_level_3.save()
                    print('boss - ', boss_level_2)
                    print('child - ', boss_level_3)
                except Exception as inst:
                    print('WARNING 3 !!!')
                    print(type(inst))
                    print(inst.args)

                count_four = 0
                for i_four in range(4):
                    count_four = count_four + 1
                    full_name, employment_date, salary_level_1, salary_level_2,\
                    salary_level_3, salary_level_4, salary_level_5 = random_generator()
                    try:
                        form = WorkerForm(data={'full_name': full_name,
                                                'position': "level 4",
                                                'employment_date': employment_date,
                                                'salary': salary_level_4
                                                }
                                          )
                        form.save()
                        current_child_len = Worker.objects.order_by('date_added')
                        current_child_id = current_child_len[(len(current_child_len) - 1)]
                        boss_level_4_id = current_child_id.id
                        boss_level_4 = Worker.objects.get(id=current_child_id.id)
                        boss_level_3 = Worker.objects.get(id=boss_level_3_id)
                        boss_level_4.move_to(boss_level_3, 'first-child')
                        boss_level_4.save()
                    except Exception as inst:
                        print('WARNING 4 !!!')
                        print(type(inst))  # the exception instance
                        print(inst.args)

                    count_five = 0
                    for i_five in range(5):
                        count_five = count_five + 1
                        full_name, employment_date, salary_level_1, salary_level_2, \
                        salary_level_3, salary_level_4, salary_level_5 = random_generator()
                        #print('count_five - ', count_five)
                        try:
                            form = WorkerForm(data={'full_name': full_name,
                                                    'position': "level 5",
                                                    'employment_date': employment_date,
                                                    'salary': salary_level_5
                                                    }
                                              )
                            print('ON line 5 ! - name - ', full_name)
                            form.save()
                            current_child_len = Worker.objects.order_by('date_added')
                            current_child_id = current_child_len[(len(current_child_len) - 1)]
                            boss_level_5 = Worker.objects.get(id=current_child_id.id)
                            boss_level_4 = Worker.objects.get(id=boss_level_4_id)
                            boss_level_5.move_to(boss_level_4, 'first-child')
                            boss_level_5.save()
                            # print(boss_level_5.full_name)
                            #print('boss - ', boss_level_4)
                            #print('child - ', boss_level_5)
                        except Exception as inst:
                            print('WARNING 5 !!!')
                            print(type(inst))  # the exception instance
                            print(inst.args)  # arguments stored in .args


run_random()
