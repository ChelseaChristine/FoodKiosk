from menuitem import MenuItem
from customer import Customer

class PlaceOrder():
    def _init_(self, ordernote, customername, date, time, ordernum, menuitem):
        self.ordernote = ordernote
        self.customer = customer
        self.date = date
        self.time = time
        self.ordernum = ordernum
        self.menuitems = []

    def getOrderNote(self):
        return self.ordernote
    
    def getCustomer(self):
        return self.customer
        
    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getOrderNum(self):
        return self.ordernum

    def addMenuItems(self,menuitem):
        self.menuitems.append(menuitem)