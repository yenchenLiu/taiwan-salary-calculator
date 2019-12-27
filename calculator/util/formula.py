class Salary:
    ordinary_incident_rate = 0.1
    employment_insurance_rate = 0.01
    health_insurance_rate = 0.0469
    salary_levels = []
    with open("salary_level.csv", "r") as f:
        lines = f.readlines()
        salary_levels = list(map(lambda l:int(l), lines))
    
    def __init__(self, salary_input):
        self.salary_level = self._get_salary_level(salary_input)

    def get_labor_level(self, min_number=11100, max_number=45800):
        return min(max(min_number, self.salary_level), max_number)

    def get_health_level(self, min_number=23800):
        return max(self.salary_level, min_number)

    def get_pension_level(self, max_number=150000):
        return min(self.salary_level, max_number)

    def get_ordinary_incident(self, load_rate=0.2):
        return round(self.get_labor_level() * self.ordinary_incident_rate * load_rate)

    def get_employment_insurance(self, load_rate=0.2):
        return round(self.get_labor_level() * self.employment_insurance_rate * load_rate)

    def get_total_labor(self):
        return self.get_ordinary_incident() + self.get_employment_insurance()

    def get_health_insurance(self, load_rate=0.3, average_number=1):
        return round(self.get_health_level() * self.health_insurance_rate * load_rate * average_number)

    def _get_salary_level(self, salary_input):
        for s in self.salary_levels:
            if s > salary_input:
                return s
        return self.salary_levels[-1]

class CompanySalary(Salary):
    injury_insurance_rate = 0.0011
    wage_debt_rate = 0.00025
    pension_rate = 0.06
    
    def get_ordinary_incident(self):
        return super().get_ordinary_incident(0.7)
    
    def get_employment_insurance(self):
        return super().get_employment_insurance(0.7)
    
    def get_injury_insurance(self):
        return round(self.get_labor_level() * self.injury_insurance_rate)
    
    def get_wage_debt(self):
        return round(self.get_labor_level() * self.wage_debt_rate)
    
    def get_total_labor(self):
        return super().get_total_labor() + self.get_injury_insurance() + self.get_wage_debt()
    
    def get_health_insurance(self):
        return super().get_health_insurance(0.6, 1.58)
    
    def get_pension(self):
        return round(self.get_pension_level() * self.pension_rate)

if __name__ == "__main__":
    salary_input = 80000
    s = Salary(salary_input)
    c = CompanySalary(salary_input)
    print(f"普通事故保險:{s.get_ordinary_incident()}")
    print(f"就業保險:{int(s.get_employment_insurance())}")
    print(f"勞保個人負擔:{s.get_total_labor()}")
    print(f"健保費用:{s.get_health_insurance()}")
    print(f"個人負擔小計:{s.get_total_labor() + s.get_health_insurance()}")
    print(f"實領薪資:{salary_input - (s.get_total_labor() + s.get_health_insurance())}")
    print(f"公司勞保負擔:{c.get_ordinary_incident()}")
    print(f"公司負擔勞保費用:{c.get_total_labor()}")
    print(f"公司負擔健保費用:{c.get_health_insurance()}")
    print(f"公司退休金負擔費用:{c.get_pension()}")
    print(f"公司負擔小計:{c.get_total_labor() + c.get_health_insurance() + c.get_pension()}")
    print(f"公司支出:{c.get_total_labor() + c.get_health_insurance() + c.get_pension() + salary_input}")
    