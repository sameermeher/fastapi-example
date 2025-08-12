from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr
from typing import Literal

app = FastAPI()

# In-memory storage
registered_users = []

class UserRegistration(BaseModel):
    username: str
    password: constr(min_length=8)
    email: EmailStr

class UserResponse(BaseModel):
    username: str
    email: EmailStr    

@app.post("/register", response_model=UserResponse)
def registerUser(payload: UserRegistration):
    username = payload.username
    password = payload.password
    email = payload.email

    for user in registered_users:
        if user["email"] == email:
            raise HTTPException(status_code=400, detail="Email already registered")

    registered_users.append({
        "username": username,
        "password": password,
        "email": email
    })
    return {"username": username, "email": email}

@app.get("/users", response_model=list[UserResponse])
def get_users():
    return [
        {
            "username": u["username"],
            "email": u["email"]
        }
        for u in registered_users
    ]