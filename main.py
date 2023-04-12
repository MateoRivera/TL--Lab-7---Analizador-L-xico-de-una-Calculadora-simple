from fastapi import FastAPI, Request
from pydantic import BaseModel
from calculator_tokenizer import tokenize
from calculator_parser import solve
import json


app = FastAPI()


class Text(BaseModel):
    expression: str


@app.post("/tokenizerCalculator")
async def text_to_tokenize(req: Text):
    return tokenize(req.expression)


@app.post("/solverCalculator")
async def text_to_solve(req: Text):
    return solve(req.expression)
