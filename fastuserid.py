from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS 설정 (React에서 접근 가능하도록)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React 개발 서버, http://localhost:5173
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청 데이터 모델
class LoginRequest(BaseModel):
    userid: str
    password: str

# 모크 데이터
MOCK_USER = {
    "userid": "user",
    "password": "1234"
}

@app.get('/')
async def root():
    return {"message": "Hello, World!"}


@app.post("/login")
async def login(request: LoginRequest):
    if request.userid != MOCK_USER["userid"]:
        msg = '사용자 아이디가 틀렸습니다'
        raise HTTPException(status_code=401, detail=msg)
    
    if request.password != MOCK_USER["password"]:
        msg = '비밀번호가 틀렸습니다'
        raise HTTPException(status_code=401, detail=msg)
    
    return {"message": "로그인 성공"}  