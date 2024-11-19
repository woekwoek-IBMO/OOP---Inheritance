class Employee:
    def __init__ (self, name, job_title, salary, year_of_exp):
        self.name=name
        self.job_title=job_title
        self.salary=salary
        self.year_of_exp=year_of_exp
    
    def change_job_title(self):
        new=input("Please enter your new job title.")
        self.job_title=new
    
    def increase_salary (self, percentage):
        self.salary+=(percentage/100)*self.salary

    def increase_yoe(self):
        self.year_of_exp += 1

    def calculate_hourly_rate (self):
        self.hourly_rate=self.salary/24

class Manager (Employee):
    def __init__(self, name, job_title, salary, year_of_exp):
        super().__init__(name,job_title,salary,year_of_exp)
        self.bonus=0

    def calculate_bonus(self):
        self.bonus=self.salary/(20-self.year_of_exp)