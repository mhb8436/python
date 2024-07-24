# 사용자로부터 기온과 날씨 상태 입력 받기
temperature = float(input("현재 기온을 입력하세요 (섭씨): "))
weather_condition = input("현재 날씨 상태를 입력하세요 (눈, 비, 맑음): ")


if temperature < 0:
    # 기온이 0도 이하일 때
    if weather_condition == "눈":
        print("눈이 오니 두꺼운 방한복과 장갑을 착용하세요.") 
    elif weather_condition == "비":
        print("비가 오니 방수 자켓과 따뜻한 옷을 입으세요.")
    else:
        print("매우 추운 날씨입니다. 두꺼운 옷을 착용하세요.")
elif 0 <= temperature < 15:
    # 기온이 0도 이상 15도 이하일 때
    if weather_condition == "눈":
        print("추운 날씨와 눈이 오니 두꺼운 외투와 장갑을 준비하세요.")
    elif weather_condition == "비":
        print("비가 오니 방수 자켓과 따뜻한 옷을 입으세요.")
    else:
        print("서늘한 날씨입니다. 가벼운 외투가 필요할 수 있습니다.")
elif 15 <= temperature < 25:
    # 기온이 15도 이상 25도 이하일 때
    if weather_condition == "눈":
        print("눈이 오지만 기온이 높으니 가벼운 외투와 스웨터를 착용하세요.")
    elif weather_condition == "비":
        print("비가 오니 우산과 가벼운 자켓을 준비하세요.")
    else:
        print("온화한 날씨입니다. 가벼운 옷이 적합합니다.")
else:
    # 기온이 25도 이상일 때
    if weather_condition == "눈":
        print("눈이 내리는 날씨는 기온이 높은 것과 어울리지 않으니 잘못된 정보일 수 있습니다.")
    elif weather_condition == "비":
        print("덥지만 비가 오니 가벼운 우산과 통기성 좋은 옷을 착용하세요.")
    else:
        print("덥고 화창한 날씨입니다. 가벼운 옷과 모자를 착용하세요.")


