
from models.order import Order

order1 = Order(23843022, 'James', '20/11/21', 6, 'Apples', 'Pink lady apples', 'Visa', 'Irvine', False, None)
order2 = Order(12314980, 'Matt', '01/11/2021', 1, 'Shoes', 'Nike Shoes, size 7', 'AMEX', 'Glasgow', True, 25)
order3 = Order(13451311, 'Lara', '03/11/2021', 2, 'Pizza', 'Just Cheese', 'Mastercard', 'London', True, 27)

orders = [order1, order2, order3]
