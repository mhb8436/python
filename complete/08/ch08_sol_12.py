# 한 주간의 날씨 데이터 (월요일부터 일요일까지)
weather_data = ['맑음', '흐림', '비', '맑음', '천둥', '비', '맑음']

#주중 날씨
print(weather_data[1:6])
#주말 날씨
print(weather_data[len(weather_data)-2:])
#수요일 부터 금요일 날씨
print(weather_data[2:5])
#마지막 3일 날씨
print(weather_data[len(weather_data)-3:])



