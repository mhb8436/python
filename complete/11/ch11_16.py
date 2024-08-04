import time

# 데코레이터 함수 정의
def time_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()  # 시작 시간 기록
        result = original_function(*args, **kwargs)  # 원래 함수 실행
        end_time = time.time()  # 종료 시간 기록
        print(f"'{original_function.__name__}' 함수 실행 시간: {end_time - start_time} 초")
        return result
    return wrapper_function

# 데코레이터를 사용할 함수 정의
@time_decorator
def example_function(duration):
    """주어진 시간(초) 동안 대기하는 함수"""
    time.sleep(duration)
    return "완료!"

# 데코레이터 적용 및 결과 확인
result = example_function(2)  # 2초 동안 대기
print(result)


