toDoList = ['세수', '이불털기', '청소', '쇼핑', '스터디', '점심먹기', '낮잠', '장보기', '넷플릭스시청']
print(toDoList)

while True:
    todo = input('끝난일=>')
    todo_index = toDoList.index(todo)
    toDoList.pop(todo_index)
    print(toDoList)
    if len(toDoList) == 0:
        break

