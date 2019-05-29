from employee import Employee

class Manager():
    def _init_(self, managerid, employee):
        self.managerid=managerid
        self.employee=employee

    def getManagerId(self):
        return self.managerid