import unittest

menu = {
    "후라이드": 18000,
    "양념치킨": 19000,
    "간장치킨": 20000
}

def get_menu():
    return menu

def order_chicken(name, quantity):
    if name not in menu:
        raise ValueError(f"{name}는/은 메뉴에 없습니다.")
    return menu[name] * quantity

class TestOrderChicken(unittest.TestCase):
    def setUp(self):
        self.menu = get_menu()

    def test_menu_is_none(self):
        self.assertIsNone(self.menu.get("마늘치킨"))

    def test_menu_is_not_none(self):
        fired = order_chicken("후라이드", 2)
        self.assertIsNotNone(fired)

    def test_price_is_correct(self):
        self.assertEqual(self.menu["양념치킨"], 19000)

    def test_total_price_is_correct(self):
        total = order_chicken("간장치킨", 2)
        self.assertEqual(total, 40000)

    def test_menu_is_unexist(self):
        with self.assertRaises(ValueError):
            order_chicken("뿌링클", 2)

    def test_menu_is_unexist_message(self):
        with self.assertRaisesRegex(ValueError, "뿌링클는/은 메뉴에 없습니다."):
            order_chicken("뿌링클", 1)


if __name__ == '__main__':
    unittest.main()