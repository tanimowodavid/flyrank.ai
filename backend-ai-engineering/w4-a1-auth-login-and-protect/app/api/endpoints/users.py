from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from app.core.supabase_client import supabase
import os


router = APIRouter(prefix="/auth", tags=["Auth"])

class UserCredentials(BaseModel):
    email: EmailStr
    password: str


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(payload: UserCredentials):
    # Explicit validation safeguard (ensures fields aren't empty strings)
    if not payload.email or not payload.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email and password are required."
        )

    try:
        # Call Supabase Auth Python method
        response = supabase.auth.sign_up({
            "email": payload.email,
            "password": payload.password
        })

        # Return user object
        if response.user:
            return {
                "message": "User registered successfully",
                "user": response.user
            }

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Registration failed."
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.post("/login", status_code=status.HTTP_200_OK)
def login(payload: UserCredentials):
    if not payload.email.strip() or not payload.password.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email and password are required."
        )

    try:
        response = supabase.auth.sign_in_with_password({
            "email": payload.email,
            "password": payload.password
        })

        # On success, extract and return access_token & refresh_token -> 200 OK
        if response.session:
            return {
                "access_token": response.session.access_token,
                "refresh_token": response.session.refresh_token,
                "token_type": "bearer"
            }

    except Exception:
        # Catch Supabase credential rejection -> 401 Unauthorized
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid login credentials"
        )

    # Fallback in case response.session is empty without raising an error
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid login credentials"
    )