import pytest

@pytest.fixture
def film_service_environment():
    print("🎥 하루 필름 서비스 환경 준비")

    users = [
        {"id": 1, "nickname": "daily_jay", "join_date": "2025-03-05"},
        {"id": 2, "nickname": "vlog_min", "join_date": "2025-02-21"}
    ]

    films = [
        {"user_id": 1, "date": "2025-03-03", "title": "카페 데이트"},
        {"user_id": 2, "date": "2025-03-03", "title": "출근길 브이로그"}
    ]

    yield  {"users": users, "films": films}

    # 3. 테스트 종료 후 로그 및 정리
    print("📝 업로드 기록 저장 완료")
    print("🧹 하루 필름 데이터 정리 완료")


def test_daily_upload(film_service_environment):
    films = film_service_environment["films"]
    user_id = 1
    upload_data =  [film["date"] for film in films if film["user_id"] == user_id]

    assert upload_data.count("2025-03-03") <= 1


def test_user_video_list(film_service_environment):
    users = film_service_environment["users"]
    films = film_service_environment["films"]

    user = users[0]  # daily_jay
    user_films = [film for film in films if film["user_id"] == user["id"]]

        # 문제3
    assert len(user_films) == 1
    # 문제4
    assert user_films[0]["title"] == "카페 데이트"