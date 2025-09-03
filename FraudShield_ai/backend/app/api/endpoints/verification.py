# --- verification.py ---
# This file defines the API endpoint for the main verification logic.


from fastapi import APIRouter, File, UploadFile, Form, Depends, HTTPException, status
from typing import Optional


from app.services.verification_orchestrator import verification_orchestrator
from app.core.security import get_api_key


# Create a new router for this endpoint
router = APIRouter()


@router.post("/verify")
async def verify_content(
   text: Optional[str] = Form(None),
   file: Optional[UploadFile] = File(None),
   # api_key: str = Depends(get_api_key) # Uncomment to enable B2B API key security
):
   """
   Main verification endpoint.
   Accepts either text or a file (video/audio) for analysis.
   This endpoint simulates the full verification pipeline.
   """
   if not text and not file:
       raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST,
           detail="Please provide either 'text' or a 'file' for analysis."
       )


   # In a real application, you would save the uploaded file temporarily to process it.
   # For this mock, we'll just use the filename.
   file_path = file.filename if file else None
  
   # Delegate the complex logic to the verification orchestrator service
   result = verification_orchestrator.run_full_verification(
       text_content=text,
       file_path=file_path
   )


   return result
