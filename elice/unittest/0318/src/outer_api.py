import requests

def get_weather(city):
    url = f"https://api.weather.com/{city}"
    response = requests.get(url)
    return response.json()


def send_weather_report(city, temperature, condition):
    url = "https://api.weather.com/report"
    data = {
        "city": city,
        "temperature": temperature,
        "condition": condition
    }
    response = requests.post(url, json=data)  # :white_check_mark: 실제 API 호출
    return response.json()  # :white_check_mark: 응답을 JSON으로 변환하여 반환