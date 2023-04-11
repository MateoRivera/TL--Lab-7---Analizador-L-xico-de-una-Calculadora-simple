from fastapi import FastAPI
from pydantic import BaseModel
from tokenizer import tokenize


app = FastAPI()


class Text(BaseModel):
    text: str


@app.post("/tokenCalculator/")
async def text_to_tokenize(body: Text):
    return tokenize(body.text)
