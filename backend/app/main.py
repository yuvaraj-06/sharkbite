from chat_gpt import GPT
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from fastapi import Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_ipaddr
from slowapi.errors import RateLimitExceeded
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

limiter = Limiter(key_func=get_ipaddr)


app = FastAPI()
pitch = GPT()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
@limiter.limit("5/second")
async def direct_pitch(request: Request):

    json_data = await request.json()
    print(json_data)
    name_pitch = json_data["pitch"]
    res = pitch.askGPT(name_pitch)
    return {"result": res}
