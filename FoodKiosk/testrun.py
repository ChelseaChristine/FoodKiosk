import unittest
from menuitem import MenuItem 
from placeorder import PlaceOrder 
from receiveorder import ReceiveOrder 

class MenuItemTest (unittest.TestCase):
    def setUp(self):
        self.menuitem = MenuItem('Small',"Burger",3.00,2)

    def test_GetItemSize(self):
        self.assertEqual(self.menuitem.getItemSize(), 'small')

    def test_GetItemName(self):
        self.assertEqual(self.menuitem.getItemName(), 'Burger')

    def test_GetItemPrice(self):
        self.assertEqual(self.menuitem.getItemPrice(), 3.00)

    def test_GetItemQuantity(self):
        self.assertEqual(self.menuitem.getItemQuantity(), 2)

class PlaceOrderTest (unittest.TestCase):
    def setUp(self):
        self.placeorder = PlaceOrder('No Pickle',"Sharon","June 4th",10:00, "order 1")
        self.item1 =PlaceOrder(self.menuitem,1)

    def test_GetOrderNote(self):
        self.assertEqual(self.placeorder.getOrderNote(), 'No Pickle')

    def test_GetCustomer(self):
        self.assertEqual(self.placeorder.getCustomer(), 'Sharon')

    def test_getDate(self):
        self.assertEqual(self.placeorder.getDate(), 'June 4th')
    
    def test_getTime(self):
        self.assertEqual(self.placeorder.getTime(), 10:00)

    def test_AddMenuItem(self):
        item =self.item1.getMenuItem()
        self.assertEqual(str(menuitem), "order 1")
