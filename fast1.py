# 비동기가 좋은 점? 동시성 여러 요청을 전부 받아주고, 효율적 처리가 가능하다는 장점이 있다
# FastAPI : RESTful API 프레임 워크  
# RESTful : (주소, 자원) 무엇을 어떻게(get, post, put, fatch, delete) 어떤 형태(json)로 주고 받을지 정의한다. 
from fastapi import FastAPI, Query
app = FastAPI(title="Hello World")

@app.get('/')  # 사용자가 요청한 주소 :http://127.0.0.1:8000/ 스키마 : 주소 : 포트 / 경로 
def root():    # 요청이 들어오면 이를 실행해 
    return {'message': 'Hello FastAPI'}

# uvicorn fast1(파일명):app(내에 앱) --reload(다시 올려줘)
# fastAPI가 보통 8000번 포트에서 사용됨

# 하나더 경로를 만듦
@app.get('/hello')   # http://127.0.0.1:8000/hello
def hello():
    return {'message': 'hello 홍길동'}

# 찾아서 죽이는 방법 : taskkill /PID 8560 /F
# 내 포트번호에 현 실행되고 있는 현황을 보고 싶을 때 : netstat -ano | findstr :8000
# 결과  netstat -ano | findstr :8000
#  TCP    127.0.0.1:8000         0.0.0.0:0              LISTENING       8560

# 동적 라우팅
# name은 변수값 
@app.get('/user/{name}')   
def hello_name(name:str) :
    return {'message': f'hello {name}'}


# + 전화 번호 
@app.get('/user/{name}/{number}')   
def hello_name(name:str, number:int) :
    return {'message': f'hello {name},  {number}'}

# 쿼리 파라미터 
# 경로에는 없지만 라우터
@app.get('/search')
def search(query:str, limit:int):  # http://127.0.0.1:8000/search?query=매개변수1&limit=매개변수2
    return {'message': f'Searching for {query} limit {limit}'}

# /search → API 경로
# ? → 쿼리 파라미터 시작
# query → 파라미터 이름
# limit -> 파라미터 이름 2
# 삼성전자 → 전달할 값
# 9999 -> 전달할 값 2 

# type hint example - list 
@app.get('/item')
def get_items(l:list[int]=Query([],  # 아이템은 최대 3개
                                min_length=1,
                                max_length=3,  
                                description="최대 3개 이상 넣지 마세요" 
                                )) :
    return {'message' : l}

# http://127.0.0.1:8000/item?l=1&l=2&l=10&l=888&l=0
# # {
#   "message": [
#     1,
#     2,
#     10,
#     888,
#     0
#   ]
# }
# type hint example 딕셔너리 
# 주의할게 딕셔너리는 get 방식으로 사용 불가, post 사용
@app.post('/item_dict')
def get_items(item:dict[str, int]) :
    return {'message' : item}

# post 방식은 body 의 내용이 화면 페이지에 보이지가 않는다. 

# str name, int 파이덴틱, 
# 상속은 basemodel로 받는다. 
# langgraph 

from pydantic import BaseModel

class Item(BaseModel) :
    name : str
    age : int 

@app.post('/itmes_class')
def get_items(item: list[Item]) :
    return {'message': item}

## py 는 서버프로그램, html은 클라이언트 프로그램

