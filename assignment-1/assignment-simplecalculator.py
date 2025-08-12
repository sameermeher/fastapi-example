from fastapi import FastAPI
from pydantic import BaseModel, validator
from typing import Literal

app = FastAPI()

class CalculatorRequest(BaseModel):
    a: float
    b: float
    operation: Literal["add", "subtract", "multiply", "divide"]

    @validator("a", "b")
    def check_number(cls, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number")
        return value

@app.post("/calculator")
def calculator(payload: CalculatorRequest):
    a = payload.a
    b = payload.b
    operation = payload.operation

    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        return a / b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return {
        "a": a,
        "b": b,
        "operation": operation,
        "result": result
    }


