from fastapi import APIRouter, status, Request, HTTPException

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

    # Token is present (not verifying validity yet as instructed)
    return {
        "message": "Access granted to profile",
        "token_received": token
    }