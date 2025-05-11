import pytest

'''
# 샘플 유저 데이터를 제공하는 fixture 정의
@pytest.fixture
def sample_user():
    #테스트에서 공통적으로 사용할 정보 셋팅
    return {"id": 1, "name": "Alice", "membership": "basic"}

def test_membership_upgrade(sample_user):
    sample_user["membership"] = "gold"

    assert sample_user["membership"] == "gold"
'''

def calculate_discount(price, rate):
    return price * (1 - rate / 100)

@pytest.mark.parametrize("price, rate, expected", [
    (10000, 10, 9000),
    (5000, 20, 4000),
    (1000, 0, 1000),
    (2000, 50, 1000)
])

def test_calculate_discount(price, rate, expected):
    assert calculate_discount(price, rate) == expected