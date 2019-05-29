class MenuItem():
    def __init__(self, itemsize, itemname, itemprice, itemquantity):
        self.itemsize=itemsize
        self.itemname=itemname
        self.iteprice=itemprice
        self.itemquantity=itemquantity

    def getItemSize(self):
        return self.itemsize

    def getItemName(self):
        return self.itemname
    
    def getItemPrice(self):
        return self.itemprice

    def getItemQuantity(self):
        return self.itemquantity
    
    def __str__(self):
        return self.itemname