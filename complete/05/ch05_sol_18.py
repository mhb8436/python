speed = int(input('자동차 주행거리를 입력하세요(km/h):'))
hour = int(input('자동차 주행시간을 입력하세요(h)'))
distance = speed * hour
msg = '기름 없음'  if distance > 460 else '기름 충분'
print(msg)

