import random

from django.core.files import File

from .forms import WorkerForm
from .models import Worker

FirstName = "Jay", "Jim", "Roy", "Axel", "Billy", "Charlie", "Jax", "Gina", "Paul",\
            "Ringo", "Ally", "Nicky", "Cam", "Ari", "Trudie", "Cal", "Carl", "Lady", "Lauren",\
            "Ichabod", "Arthur", "Ashley", "Drake", "Kim", "Julio", "Lorraine", "Floyd", "Janet",\
            "Lydia", "Charles", "Pedro", "Bradley", "Aaron", "Abraham", "Adam", "Adrian", "Aidan",\
            "Alan", "Albert", "Alejandro", "Alex", "Alexander", "Alfred", "Andrew", "Angel", "Anthony",\
            "Antonio", "Ashton", "Austin", "Daniel", "David", "Dennis", "Devin", "Diego", "Dominic",\
            "Donald", "Douglas", "Dylan", "Harold", "Harry", "Hayden", "Henry", "Herbert", "Horace",\
            "Howard", "Hugh", "Hunter", "Malcolm", "Martin", "Mason", "Matthew", "Michael", "Miguel",\
            "Miles", "Morgan"


LastName = "Barker", "Style", "Spirits", "Murphy", "Blacker", "Bleacher", "Rogers",\
           "Warren", "Keller", "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis",\
           "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez",\
          "Moore", "Martin", "Jackson", "Thompson", "White", "Lopez", "Lee", "Gonzalez", "Harris",\
         "Clark", "Lewis", "Robinson", "Walker", "Perez", "Hall", "Young", "Allen", "Sanchez",\
         "Wright", "King", "Scott", "Green", "Baker", "Adams", "Nelson", "Hill", "Ramirez", "Campbell",\
         "Mitchell", "Roberts", "Carter", "Phillips", "Evans", "Turner", "Torres", "Parker", "Collins",\
         "Edwards", "Stewart", "Flores", "Morris", "Nguyen", "Murphy", "Rivera", "Cook", "Rogers",\
         "Morgan", "Peterson", "Cooper", "Reed", "Bailey", "Bell", "Gomez", "Kelly", "Howard", "Ward",\
         "Cox", "Diaz", "Richardson", "Wood", "Watson", "Brooks", "Bennett", "Gray", "James", "Reyes",\
         "Cruz", "Hughes", "Price", "Myers", "Long", "Foster", "Sanders", "Ross", "Morales", "Powell",\
         "Sullivan", "Russell", "Ortiz", "Jenkins", "Gutierrez", "Perry", "Butler", "Barnes", "Fisher",\
         "Henderson", "Coleman", "Simmons", "Patterson", "Jordan", "Reynolds", "Hamilton", "Graham",\
         "Kim", "Gonzales", "Alexander", "Ramos", "Wallace", "Griffin", "West", "Cole", "Hayes", "Chavez",\
         "Gibson", "Bryant", "Ellis", "Stevens", "Murray", "Ford", "Marshall", "Owens", "McDonald", "Harrison",\
         "Ruiz", "Kennedy", "Wells", "Alvarez", "Woods", "Mendoza", "Castillo", "Olson", "Webb", "Washington",\
         "Tucker", "Freeman", "Burns", "Henry", "Vasquez", "Snyder", "Simpson", "Crawford", "Jimenez",\
         "Porter", "Mason", "Shaw", "Gordon", "Wagner", "Hunter", "Romero", "Hicks", "Dixon", "Hunt",\
         "Palmer", "Robertson", "Black", "Holmes", "Stone", "Meyer", "Boyd", "Mills", "Warren", "Fox",\
         "Rose", "Rice", "Moreno", "Schmidt", "Patel", "Ferguson", "Nichols", "Herrera", "Medina", "Ryan",\
         "Fernandez", "Weaver", "Daniels", "Stephens", "Gardner", "Payne", "Kelley", "Dunn", "Pierce",\
         "Arnold", "Tran", "Spencer", "Peters", "Hawkins", "Grant", "Hansen", "Castro", "Hoffman", "Hart",\
         "Elliott", "Cunningham", "Knight", "Bradley"


Salary_level_1 = "15000", "14000", "17000"
Salary_level_2 = "10000", "11000", "10500", "9500", "9700", "9200"
Salary_level_3 = "7500", "6500", "6700", "6900", "6850", "7250", "7450", "7350", "7150", "6800"
Salary_level_4 = "4000", "5000", "4200", "4300", "4450", "4550", "4250", "4150", "4600", "4700"
Salary_level_5 = "2000", "3000", "2200", "2300", "2450", "2550", "2250", "2150", "2600", "2700"

Day = "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",\

Month = "01", "02", "03", "04", "05", "06", "07", "08",\
        "09", "10", "11", "12"

Year = "2016", "2017", "2018"

folder_name = 'media\ '

folder_name = folder_name.strip()


img_file_name = "001", "002", "003", "005", "006", "007", "008", "009", "010"


def run_random():
    count_one = 0
    for i_one in range(5):
        count_one = count_one + 1
        # print('count_one - ', count_one)
        First = random.choice(FirstName)
        Last = random.choice(LastName)
        Employee_Salary_level_1 = random.choice(Salary_level_1)
        Employee_Year = random.choice(Year)
        Employee_Month = random.choice(Month)
        Employee_Day = random.choice(Day)
        form = WorkerForm(data={'full_name': First + ' ' + Last, 'position': "level 1", 'employment_date': Employee_Year + '-' + Employee_Month + '-' + Employee_Day, 'salary': Employee_Salary_level_1})
        form.save()
        current_child_len = Worker.objects.order_by('date_added')
        current_child_id = current_child_len[(len(current_child_len) - 1)]
        boss_level_1_id = current_child_id.id
        boss_level_1 = Worker.objects.get(id=current_child_id.id)
        # print(boss_level_1.full_name)
        boss_level_1.move_to(None, 'left')
        boss_level_1.save()

        count_two = 0
        for i_two in range(3):
            count_two = count_two + 1
            # print('count_two - ', count_two)
            First = random.choice(FirstName)
            Last = random.choice(LastName)
            Employee_Salary_level_2 = random.choice(Salary_level_2)
            Employee_Year = random.choice(Year)
            Employee_Month = random.choice(Month)
            Employee_Day = random.choice(Day)
            try:
                form = WorkerForm(data={'full_name': First + ' ' + Last,
                                        'position': "level 2",
                                        'employment_date': Employee_Year + '-' + Employee_Month + '-' + Employee_Day,
                                        'salary': Employee_Salary_level_2
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
                #print('boss - ', boss_level_1)
                #print('child - ', boss_level_2)
            except:
                print('WARNING 2 !!!')

            count_three = 0
            for i_three in range(3):
                count_three = count_three + 1
                #print('count_three - ', count_three)
                First = random.choice(FirstName)
                Last = random.choice(LastName)
                Employee_Salary_level_3 = random.choice(Salary_level_3)
                Employee_Year = random.choice(Year)
                Employee_Month = random.choice(Month)
                Employee_Day = random.choice(Day)
                try:
                    form = WorkerForm(data={'full_name': First + ' ' + Last,
                                            'position': "level 3",
                                            'employment_date': Employee_Year + '-' + Employee_Month + '-' + Employee_Day,
                                            'salary': Employee_Salary_level_3
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
                except:
                    print('WARNING 3 !!!')

                count_four = 0
                for i_four in range(4):
                    count_four = count_four + 1
                    #print('count_four - ', count_four)
                    First = random.choice(FirstName)
                    Last = random.choice(LastName)
                    Employee_Salary_level_4 = random.choice(Salary_level_4)
                    Employee_Year = random.choice(Year)
                    Employee_Month = random.choice(Month)
                    Employee_Day = random.choice(Day)
                    try:
                        form = WorkerForm(data={'full_name': First + ' ' + Last,
                                                'position': "level 4",
                                                'employment_date': Employee_Year + '-' + Employee_Month + '-' + Employee_Day,
                                                'salary': Employee_Salary_level_4
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
                        #print('boss - ', boss_level_3)
                        #print('child - ', boss_level_4)
                    except:
                        print('WARNING 4 !!!')

                    count_five = 0
                    for i_five in range(5):
                        count_five = count_five + 1
                        #print('count_five - ', count_five)
                        First = random.choice(FirstName)
                        Last = random.choice(LastName)
                        Employee_Salary_level_5 = random.choice(Salary_level_5)
                        Employee_Year = random.choice(Year)
                        Employee_Month = random.choice(Month)
                        Employee_Day = random.choice(Day)
                        try:
                            form = WorkerForm(data={'full_name': First + ' ' + Last,
                                                    'position': "level 5",
                                                    'employment_date': Employee_Year + '-' + Employee_Month + '-' + Employee_Day,
                                                    'salary': Employee_Salary_level_5
                                                    }
                                              )
                            print('ON line 5 ! - name - ', First, '', Last)
                            form.save()
                            current_child_len = Worker.objects.order_by('date_added')
                            current_child_id = current_child_len[(len(current_child_len) - 1)]
                            #boss_level_5_id = current_child_id.id
                            boss_level_5 = Worker.objects.get(id=current_child_id.id)
                            boss_level_4 = Worker.objects.get(id=boss_level_4_id)
                            boss_level_5.move_to(boss_level_4, 'first-child')
                            boss_level_5.save()
                            #print('boss - ', boss_level_4)
                            #print('child - ', boss_level_5)
                        except Exception as inst:
                            print(type(inst))  # the exception instance
                            print(inst.args)  # arguments stored in .args
                            print(inst)
                            print('WARNING 5 !!!')



run_random()
