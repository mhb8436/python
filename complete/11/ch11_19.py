def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 함수 호출
print_kwargs(name="Alice", age=30)
print_kwargs(city="Seoul", country="Korea", population=10000000)



