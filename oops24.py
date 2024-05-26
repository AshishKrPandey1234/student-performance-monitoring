class Employee:
    company_name="infosys"
    def __init__(self,nm,sal):
        self.nm=nm
        self.sal=sal
    @classmethod
    def get_companyname(cls):
        print(f"company name is ",cls.company_name)
e1=Employee('jay',30000)
e2=Employee("vijay",35000)
Employee.get_companyname()
print(e2.company_name)