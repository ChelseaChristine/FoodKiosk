from employee import Employee
from placeorder import PlaceOrder

class ReceiveOrder():
    def _init_(self, employeeid, orderitem, time):
        self.employeeid=employeeid
        self.orderitem=orderitem
        self.time=time
    
    def getEmployeeId(self):
        return self.employeeid

    def getOrderItem(self):
        return self.orderitem

    def getTime(self):
        return self.time

    

