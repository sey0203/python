from faker import Faker
import random
from datetime import date

fake = Faker('ko_KR')

BROADCASTERS = ["KBS", "MBC", "SBS", "Mnet"]
GROUPS = ["BTS", "BLACKPINK", "NEWJEANS", "IVE", "LE SSERAFIM"]
SONGS = {
    "BTS": ["Dynamite", "Butter", "IDOL"],
    "BLACKPINK": ["DDU-DU DDU-DU", "Pink Venom", "Shut Down"],
    "NEWJEANS": ["OMG", "Super Shy", "Ditto"],
    "IVE": ["ELEVEN", "LOVE DIVE", "Baddie"],
    "LE SSERAFIM": ["ANTIFRAGILE", "UNFORGIVEN", "Perfect Night"]
}
CONCEPTS = ["Y2K 감성", "블랙시크", "한복무대", "스포티 룩", "글리터 파티"]
CHANTS = ["하나 둘 셋, {} 최고!", "{} 사랑해!", "{} 화이팅!"]

# start_date = date(2025, 1, 1)
# end_date = date(2025, 3, 12)


def idol_data(num):
    data = []
    for _ in range(num):
        date = fake.date_this_year()
        broadcaster = fake.random_element(BROADCASTERS)
        group = fake.random_element(GROUPS)
        titlesong = fake.random_element(SONGS[group])
        concept = fake.random_element(CONCEPTS)
        fan_chant = fake.random_element(CHANTS).format(group)

        entry = {
            "date": date,
            "broadcaster": broadcaster,
            "group": group,
            "titlesong": titlesong,
            "concept": concept,
            "fan_chant": fan_chant
        }

        data.append(entry)

    return data

if __name__ == "__main__":
    for entry in idol_data(5):
        print(entry)

def test_result_not_none():
    assert idol_data()