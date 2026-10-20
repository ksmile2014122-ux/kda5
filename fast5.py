from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# 사진 업로드 

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}

# 위의 소스 실행 버전
# STEP 1: Import the necessary modules.
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.components import processors
from mediapipe.tasks.python import vision
from fastapi import FastAPI,File, UploadFile
import numpy as np
import cv2  # 만약 없다면 , uv add opencv-python numpy

# STEP 2: Create an ImageClassifier object.
base_options = python.BaseOptions(model_asset_path='model\\efficientnet_lite0.tflite')
options = vision.ImageClassifierOptions(
    base_options=base_options, max_results=4)
classifier = vision.ImageClassifier.create_from_options(options)


app = FastAPI()

@app.post("/uploadfile/")
async def upload_file(file:UploadFile):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)

    # STEP 4: Classify the input image.
    classification_result = classifier.classify(image)

    # STEP 5: Process the classification result. In this case, visualize it.
    top_category = classification_result.classifications[0].categories[0]
    ret = f"{top_category.category_name} ({top_category.score:.2f})"
    return ret

# react 는 쉽게 만들수 있나 ui framework 라고 생각
# css 어디에 예쁘게 나둘것인가
# javascrip 이벤트 발생 코드,   정적인 페이지를 동적인 페이지로 만들어주는 아이 
# 자바스크립트 : 버튼 동작시 발생 
# 내가 만드는 HTML과 CSS를 어떻게 연결을 할지?? 

