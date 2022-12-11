class Manager:
    def __init__(self, boolean):
        self.boolean = boolean
        
    def __init__(self, name, salary, exp):
        self.name = name
        self.salary = salary
        self.exp = exp
        
    def __int__(self, oversee, organize, pay_salary):
        self.oversee = oversee
        self.organize = organize
        self.pay_salary = pay_salary
    
    def __str__(self):
        return f"{self.name} has {self.exp} and get {self.salary} dollar a year"
        
        
class Worker:
    def __init__(self, depart, rate, amount_raised, capability):
        self.depart = depart
        self.rate = rate
        self.amount_raised = amount_raised
        self.capability = capability
        
    def __str__(self):
        return f"{self.depart} has {self.rate} salary rate and raise {self.amount_raised}% per year, this {self.depart} does {self.capability}"
    
x = Worker('Accounting', 3000, 3, 'tax')

print(x)
        