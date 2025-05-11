import random

MBTI_PROFILES = {
    "ENFP": {"attend_rate": (80, 100), "leave_early_rate": (10, 30), "favorite_menu": ["감바스", "피자", "치킨"]},
    "ISTJ": {"attend_rate": (30, 60), "leave_early_rate": (60, 90), "favorite_menu": ["삼겹살", "갈비", "해물탕"]},
    "INFJ": {"attend_rate": (40, 70), "leave_early_rate": (50, 70), "favorite_menu": ["비건 샐러드", "파스타", "샤브샤브"]},
    "ENTP": {"attend_rate": (70, 90), "leave_early_rate": (20, 40), "favorite_menu": ["떡볶이", "삼겹살", "회"]},
    "ISFP": {"attend_rate": (50, 80), "leave_early_rate": (30, 60), "favorite_menu": ["스테이크", "초밥", "버거"]}
}

AllMBTI = list(MBTI_PROFILES.keys())

def extract_random_mbti(num_sample = 10):
    data = []
    for _ in range(num_sample):
        mbti = random.choice(AllMBTI)
        profile = MBTI_PROFILES[mbti]

        attend_rate = random.randint(*profile["attend_rate"])
        leave_early_rate = random.randint(*profile["leave_early_rate"])
        favorite_menu = random.choice(profile["favorite_menu"])

        mood_maker = "O" if mbti.startswith("E") else "X"

        entry = {
            "MBTI": mbti,
            "attend_rate": attend_rate,
            "leave_early_rate": leave_early_rate,
            "favorite_menu": favorite_menu,
            "mood_maker": mood_maker
        }

        data.append(entry)

    return data


# if __name__ == "__main__":
#     for entry in extract_random_mbti(10):
#         print(entry)