import re

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
text = "제품에 문제가 있으면 support@example.com 으로 연락주세요"
match = re.search(pattern, text)

if match:
    print('Email Found :', match.group())
else:
    print('No Email Found')


