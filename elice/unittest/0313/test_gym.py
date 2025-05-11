import unittest


class GymMemberDB():
    def __init__(self):
        self.members = {}

    def connect(self):
        print("💪 GYM BRO 전용 DB 연결 완료")

    def close(self):
        print("💪 GYM BRO 전용 DB 연결 종료")

    def add_member(self, username, info):
        self.members[username] = info

    def update_member(self, username, info):
        if username not in self.members:
            raise ValueError("존재하지 않는 GYM BRO입니다.")
        self.members[username] = info

    def get_member(self, username):
        return self.members.get(username)
    
    def delete_member(self, username):
        if username in self.members:
            del self.members[username]

class TestGym(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("🏋‍♂ GYM BRO 환경 세팅 시작")
        cls.db = GymMemberDB()
        cls.db.connect()

    @classmethod
    def tearDownClass(cls):
        print("🏋‍♂ GYM BRO 환경 마무리")
        cls.db.close()

    def setUp(self):
        print("🔥 각 테스트마다 기본 GYM BRO 등록")
        self.db.add_member("g-dragon", {"name":"지드래곤", "level":"Standard"})

    def tearDown(self):
        print("🧹 테스트 끝! GYM BRO 데이터 정리")
        self.db.delete_member("g-dragon")

    def test_add_member(self):
        self.db.add_member("taeyang", {"name":"태양", "level":"Standard"})
        new_mem = self.db.get_member("taeyang")
        self.assertEqual(new_mem["name"], "태양")

    def test_update_member(self):
        self.db.update_member("g-dragon", {"name":"지드래곤", "level":"VIP"})
        update_mem = self.db.get_member("g-dragon")
        self.assertEqual(update_mem["level"], "VIP")

    def test_get_nonexistent_gym(self):
        self.assertIsNone(self.db.get_member("unknown_boy"))

    def test_delete_member(self):
        self.db.delete_member("g-dragon")
        self.assertIsNone(self.db.get_member("g-dragon"))