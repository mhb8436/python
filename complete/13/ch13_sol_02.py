# 스마트폰 클래스를 정의합니다.
class Smartphone:
    def __init__(self, model, manufacturer, storage, battery):
        self.model = model
        self.manufacturer = manufacturer
        self.storage = storage
        self.battery = battery

    def call(self, number):
        print(f"{self.model}에서 {number}로 전화를 겁니다.")

    def send_message(self, number, message):
        print(f"{self.model}에서 {number}로 '{message}' 문자를 보냅니다.")

    def take_photo(self):
        print(f"{self.model}로 사진을 찍습니다.")

    def charge_battery(self):
        self.battery = 100
        print(f"{self.model}의 배터리가 충전되었습니다. 현재 배터리 상태: {self.battery}%")

# 내 스마트폰 객체를 생성합니다.
my_phone = Smartphone("iPhone 13", "Apple", "128GB", 75)

# 친구의 스마트폰 객체를 생성합니다.
friends_phone = Smartphone("Galaxy S21", "Samsung", "256GB", 50)

# 내 스마트폰의 행동을 실행합니다.
my_phone.call("010-1234-5678")
my_phone.send_message("010-1234-5678", "안녕하세요!")
my_phone.take_photo()
my_phone.charge_battery()

# 친구의 스마트폰의 행동을 실행합니다.
friends_phone.call("010-8765-4321")
friends_phone.send_message("010-8765-4321", "반가워요!")
friends_phone.take_photo()
friends_phone.charge_battery()



