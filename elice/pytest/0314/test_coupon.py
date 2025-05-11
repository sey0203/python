import pytest
from coupon import apply_coupon

def test_apply_valid_coupon():
    assert apply_coupon(10000, 20) == 8000

def test_apply_zero_coupon():
    assert apply_coupon(10000, 0) == 10000

def test_apply_full_coupon():
    assert apply_coupon(10000, 100) == 0

def test_invalid_coupon_rate():
    with pytest.raises(ValueError):
        apply_coupon(10000, 150)

# if __name__ == '__main__':
#     pytest.main()