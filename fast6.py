#fast_jinja.py

# 개발중일때 fastapi dev fast6.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

#루트 경로를 의미 브라우저에서 http://127.0.0.1:8000/로 접근할 때 실행되는 함수
@app.get("/", response_class=HTMLResponse) 
async def read_item(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"message": "Hello, FastAPI"}
    )

# 