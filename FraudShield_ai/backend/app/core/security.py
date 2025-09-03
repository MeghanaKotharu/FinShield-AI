# --- security.py ---
# This file handles the security aspects of the API, such as API key validation.


from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader


from app.core.config import settings


# Define the name of the header where the API key is expected.
# The client should send the key in the format: "Authorization: Bearer <YOUR_API_KEY>"
api_key_header = APIKeyHeader(name="Authorization")


def get_api_key(authorization: str = Security(api_key_header)) -> str:
   """
   Dependency function to validate the API key from the Authorization header.
  
   This function is used in API endpoints to protect them. It checks:
   1. If the Authorization header is present.
   2. If the header format is "Bearer <key>".
   3. If the provided <key> is in the list of allowed keys.
  
   Raises:
       HTTPException: If any of the checks fail.
      
   Returns:
       str: The validated API key if successful.
   """
   # Check if the header format is correct
   if not authorization.startswith("Bearer "):
       raise HTTPException(
           status_code=status.HTTP_401_UNAUTHORIZED,
           detail="Invalid authorization scheme. Must be 'Bearer'."
       )
  
   # Extract the key from the "Bearer <key>" string
   api_key = authorization.split(" ")[1]


   # Check if the provided key is in our list of allowed keys
   if api_key not in settings.ALLOWED_API_KEYS:
       raise HTTPException(
           status_code=status.HTTP_401_UNAUTHORIZED,
           detail="Invalid or missing API Key"
       )
  
   return api_key




