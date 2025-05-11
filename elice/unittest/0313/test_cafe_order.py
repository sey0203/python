import unittest

menu = {
    "아메리카노": 4000,
    "카페라떼": 4500,
    "딸기라떼": 5000
}


def order_drink(name, quantity):
    if name not in menu:
        raise ValueError(f"{name}는 판매하지 않는 메뉴입니다.")
    return menu[name] * quantity

class TestOrder(unittest.TestCase):

    def setUp(self):
        self.menu = menu

    def test_price(self):
        self.assertEqual(self.menu["딸기라떼"], 5000)

    def test_total_price(self):
        total = order_drink("아메리카노", 2)
        self.assertEqual(total, 8000)

    def test_menu_exist(self):
        self.assertTrue(self.menu, "카페라떼")

    def test_menu_unexist(self):
        with self.assertRaises(ValueError):
            order_drink("자몽주스", 2)

    def test_menu_unexist_message(self):
        with self.assertRaisesRegex(ValueError, "자몽주스는 판매하지 않는 메뉴입니다."):
            order_drink("자몽주스", 1)
    
    def tearDown(self):
        self.menu = None