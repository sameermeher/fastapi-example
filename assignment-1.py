from fastapi import FastAPI
from pydantic import BaseModel, validator
from typing import Any

app = FastAPI()

class MultiplyRequest(BaseModel):
    a: Any
    b: Any

    @validator("a","b")
    def check_integer(cls, value):
        if not isinstance(value, int):
            raise ValueError("Value must be integer")
        return value

@app.post("/multiply")
def multiply_numbers(payload: MultiplyRequest):
    return payload.a * payload.b


