# TO-do-list 만들기
# 1. 아침먹기 : true 
# 2. 점심먹기 : false
# 3. 저녁먹기 : false
# 조회값에 따라 desc 하게 정렬할지, asc 하게 정렬할지 
# ㅣ = [1,2,3]
# ㅣ[start:end:stop]
# 1. 전체 todo리스트 보기 
# 2. asc / desc
# 3. 특정 id만 조회 
# 4. 특정한 id만 수정 
# 5. 특정한 id만 삭제 
# patch 일부만 수정, delete 일부 삭제
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# 키, 값, True/False
todo_list = {1 : {'id': 1, 'content': '아침먹기', 'done' : True},
            2: {'id': 2, 'content': '점심먹기', 'done' : False},
            3: {'id': 3, 'content': '저녁먹기', 'done' : False}}

# todos의 전체 조회 
@app.get('/')
def todos():
    return list(todo_list.values())

# todos의 전체 조회- 조건 ASC/DESC
@app.get('/todos')
def get_todos(order:str ='ASC'):
    if order and order.upper() == 'DESC' :
        l = list(todo_list.values())
        return list(l[::-1])  # 내림차순으로 변경
    return list(todo_list.values())

# todos 중 하나만 들고 오기
@app.get('/todo/{no}')
def get_todo(no:int = 1):  # defalut 로 1을 줌 
    return todo_list.get(no, {})

# 
class todoRequest(BaseModel) :
    id : int
    content : str
    done : bool 

# 입력 해보기 : 4. 야식먹기 , False
@app.post('/todo/{no}')  #get 과 post는 다른 방식의 메서드라서 경로는 같아도 상관 없음
def create_todo(request: todoRequest): #데이터 형식을 알려줘 
    todo_list[request.id] = request.model_dump()
    return todo_list[request.id]
from typing import Annotated
from fastapi import Body


# 수정 
@app.patch("/todos/{todo_id}")
def update_todo(todo_id: int, is_done: Annotated[bool, Body(embed=True)]) -> dict:
    todo = todo_list.get(todo_id)
    if todo:
        todo["is_done"] = is_done
        return todo
    return {}

# 삭제 
@app.delete('/todos/{todo_id}')
def delet_todo(todo_id:int)-> list[dict]:
    todo_list.pop(todo_id, None) #키 오류 방지
    return todo_list

