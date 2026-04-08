from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

from prompt_engine import generate_prompt
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# 요청 데이터 구조
class PromptRequest(BaseModel):
    preview_text: str
    style: str


# API 엔드포인트
@app.post("/generate")
def generate_prompt_api(req: PromptRequest):
    result, _ = generate_prompt(req.preview_text, req.style)
    return {"result": result}