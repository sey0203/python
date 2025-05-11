import unittest
import random

def generate_nickname(pool):
    if not pool:
        raise ValueError("닉네임 후보가 없습니다.")
    return random.choice(pool)

class TestNickname(unittest.TestCase):
    def setUp(self):
        pool = ["gd", "ty", "ds"]
        self.pool = pool

    def tearDown(self):
        self.pool = None

    def test_nickname_is_exist(self):
        result = generate_nickname(self.pool)
        self.assertIn(result, self.pool)

    def test_invalid_nickname(self):
        with self.assertRaises(ValueError):
            generate_nickname([])