def apply_coupon(price, coupon_rate):
    if not (0 <= coupon_rate <= 100):
        raise ValueError("쿠폰 할인율은 0~100% 사이여야 합니다.")
    return price * (1 - coupon_rate / 100)