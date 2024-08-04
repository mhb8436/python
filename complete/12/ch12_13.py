import re

pattern = r"hello"
text = "hello world "
match = re.match(pattern, text)
if match:
    print('Match Found')
else:
    print('No Match Found')

pattern = r"hello"
text = "hello world "
match = re.search(pattern, text)
if match:
    print('Match Found')
else:
    print('No Match Found')

pattern = r"\d+"
text = "123 개의 사과와 456 개의 귤이 있습니다."
matches = re.findall(pattern, text)
print(matches)