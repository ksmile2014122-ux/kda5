from fastapi import FastAPI, Query, Path, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import random
from datetime import datetime
import datetime
from enum import Enum

app = FastAPI(title="Hello World")


# 1-1. 실습
@app.get('/')  # 사용자가 요청한 주소 :http://127.0.0.1:8000/ 스키마 : 주소 : 포트 / 경로 
def root():    # 요청이 들어오면 이를 실행해 
    return {'message': '키움 디지털 아카데미 5기에 오신 것을 환영합니다.', 
            "학습_단계": [
                "1단계: 기본 GET 요청",
                "2단계: 경로 매개변수",
                "3단계: 쿼리 매개변수",
                "4단계: POST 요청과 모델",
                "5단계: 실전 프로젝트"
            ],
            "tip" : "/docs 에서 API 문서를 확인해보세요!" }

# 1-3. 실습 

@app.get('/user/{name}') 
def get_greet( name : str) :
    lucky_number = random.randint(1,100) 
    today = datetime.today().strftime("%Y-%m-%d")
    greetings = random.choice(["안녕하세요", "반갑습니다", "환영합니다", "좋은 하루예요"])
    
    return {'message': f'{greetings} , {name}',
            "today" : f'{today}',
            "lucky_number" : f"{lucky_number}"
            }

# 1-3 : 실습, class 로 해보기  

class Hello(BaseModel) : 
    message : str
    today : datetime.date
    lucky_number : int = Field(ge =1, le =100)

@app.get('/hello1/{name}', response_model= Hello)   
def hello1(name : str)-> Hello :  # input -> output 
    greetings = random.choice(["안녕하세요", "반갑습니다", "환영합니다", "좋은 하루예요"])
    return Hello(
        message= f'{greetings}, {name}',
        today= datetime.date.today(), 
        lucky_number= random.randint(1,100) 
    )


# 1-2 : 사칙연산 
# operate 사칙연산 관련된 class하나
# request 요청 관련된 class하나
# response 응답 관련된 class하나
# 함수 -> 사칙연산을 위한 함수 

from fastapi import FastAPI, Query

from enum import Enum

from pydantic import BaseModel

app = FastAPI(title="Hello World")

@app.get('/operate')
def root():
    return {'message':'Hello FastAPI'}

#사칙연산 class
class Operator(str, Enum):
    add = "add"
    sub = "sub"
    mul = "mul"
    div = "div"

#요청하는 클래스

class c_Request(BaseModel):
    op : Operator
    a : float
    b : float

#응답하는 클래스

class c_Response(BaseModel):
    op : Operator
    a : float
    b : float
    result : float  # 결과값의 타입을 class로 지정

#함수 -> 4칙연산을 위한 함수

def calculate(a, b, op) -> float:
    if op == Operator.add:
        result = a + b
    elif op == Operator.sub:
        result = a - b
    elif op == Operator.mul:
        result = a * b
    elif op == Operator.div:
        result = a / b
    return result

@app.get('/calc/{op}', response_model=c_Response) # 결과값의 타입을 class로 지정 
def calc_get(op:Operator, a: float, b : float) :
    result = calculate(a, b, op)
    return c_Response(op=op, a=a, b=b, result=result)

# 사칙연산 사용법 :  http://127.0.0.1:8000/calc/mul?a=10&b=100
