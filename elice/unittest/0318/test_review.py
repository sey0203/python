import unittest

def add_review(food = "라면", star = 0, comment = "인사"):
    if food == None or star == None or comment == None:
        return None
    
    if not (1 <= star <= 5):
        raise ValueError("별점은 1~5점 사이여야 합니다.")
    
    if len(comment) < 5:
        raise ValueError("리뷰는 최소 5자 이상이어야 합니다.")
    return f"{food}: {'★' * star} - {comment}"

class TestReview(unittest.TestCase):
    def test_review_is_correct(self):
        food = "라면"
        star = 3
        comment = '너무 맛있어요!!'

        result = add_review(food, star, comment)
        must_result = f"{food}: {'★' * star} - {comment}"
        self.assertEqual(result, must_result)

    def test_review_is_fail(self):
        with self.assertRaises(ValueError):
            add_review()

    def test_add_review_none(self):
        self.assertIsNone(add_review(None, None))

    def test_add_review_not_none(self):
        food = "라면"
        star = 3
        comment = '너무 맛있어요!!'

        result = add_review(food, star, comment)
        self.assertIsNotNone(result)

    def test_add_review_in_str(self):
        food = "라면"
        star = 3
        comment = '너무 맛있어요!!'

        result = add_review(food, star, comment)
        self.assertIn(comment, result)

