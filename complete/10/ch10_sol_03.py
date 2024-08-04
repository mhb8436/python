def avgSpeed():
    print('평균 속도(km/h) : ', format(distance / hour, '.2f'))


hour = int(input('여행한 시간(h):'))
distance = int(input('여행한 거리(km):'))

avgSpeed()


