# 로깅 데코레이터 함수 정의
def logging_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"'{original_function.__name__}' 
              함수가 호출됨: args={args}, kwargs={kwargs}")
        result = original_function(*args, **kwargs)
        print(f"'{original_function.__name__}' 
              함수가 반환한 값: {result}")
        return result
    return wrapper_function

# 데코레이터를 사용할 함수 정의
@logging_decorator
def add(a, b):
    """두 숫자의 합을 반환하는 함수"""
    return a + b

@logging_decorator
def greet(name, greeting="안녕하세요"):
    """인사를 반환하는 함수"""
    return f"{greeting}, {name}!"

# 데코레이터 적용 및 결과 확인
result_add = add(5, 3)  # add 함수 호출
print(result_add)

result_greet = greet("철수")  # greet 함수 호출
print(result_greet)

result_greet_custom = greet("영희", 
    greeting="반갑습니다")  # greet 함수 호출
print(result_greet_custom)



