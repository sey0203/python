import pytest

class Recommander():
  def get_recommnd(self, mbti, situation):
    recommendations = {
        "ENFP": {
           "주말": "인턴",
            "퇴근 후": "라라랜드",
            "비 오는 날": "비포 선라이즈"
        },
        "INFJ": {
            "주말": "리틀 포레스트",
            "퇴근 후": "월터의 상상은 현실이 된다",
            "비 오는 날": "어바웃 타임"
        }
  }
    return recommendations.get(mbti, {}).get(situation, "추천 없음")
  
@pytest.fixture
def recommandation():
    return Recommander()

@pytest.mark.parametrize("mbti, situation, expected_movie", [
    ("ENFP", "주말", "인턴"),
    ("ENFP", "퇴근 후", "라라랜드"),
    ("ENFP", "비 오는 날", "비포 선라이즈"),
    ("INFJ", "주말", "리틀 포레스트"),
    ("INFJ", "퇴근 후", "월터의 상상은 현실이 된다"),
    ("INFJ", "비 오는 날", "어바웃 타임"),
    ("ISTP", "주말", "추천 없음"),
])

def test_mbti_movie_recommandation(recommandation, mbti, situation, expected_movie):
    result = recommandation.get_recommnd(mbti, situation)
    assert result == expected_movie