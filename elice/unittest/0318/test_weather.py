import unittest
from unittest.mock import Mock, patch
import src.outer_api as outer_api


class TestWeatherAPI(unittest.TestCase):
  #requests 모듈파일음. -> requests -> get => mock객체(가짜 데이터 담당하는 기능)
  @patch("outer_api.requests.get")
  def test_weather_api(self, mock_get: Mock): 
    mock_get.return_value.json.return_value = {"temp": 25, "condition": "Sunny"}
    result = outer_api.get_weather("Seoul") #실제 함수를 가동한다!!
    #호출부를 제외한 모든 로직 테스트 + 호출 가짜 호출 
    
    self.assertEqual(result, {"temp": 25, "condition": "Sunny"})
    mock_get.assert_called_once_with("https://api.weather.com/Seoul")

    mock_get.side_effect = TimeoutError() #에러발생한다. #계염령 
    with self.assertRaises(TimeoutError):
      outer_api.get_weather("Seoul") #실제 함수를 가동한다!!