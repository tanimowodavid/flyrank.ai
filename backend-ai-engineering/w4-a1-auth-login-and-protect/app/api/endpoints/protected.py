from fastapi import APIRouter, status, Request, HTTPException
from app.core.supabase_client import supabase

router = APIRouter(prefix="/protected", tags=["Protected"])


@router.get("/profile", status_code=status.HTTP_200_OK)
def protected_profile(request: Request):
    # Extract the Authorization header manually
    auth_header = request.headers.get("Authorization")

    # Check if header is missing
    if not auth_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access token required"
        )

    # Split into scheme and token ("Bearer <token>")
    parts = auth_header.strip().split()

    # Check if header is malformed or missing the actual token string
    if len(parts) != 2 or parts[0].lower() != "bearer" or not parts[1].strip():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access token required"
        )

    token = parts[1]

    # Verify token with Supabase Auth
    try:
        response = supabase.auth.get_user(token)

        # Ensure user object exists in response
        if not response or not response.user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token"
            )

        user = response.user

        # Return safe metadata -> 200 OK
        return {
            "id": user.id,
            "email": user.email,
            "created_at": user.created_at
        }

    except Exception:
        # Catches network errors, expired JWTs, tampered signatures, etc.
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )