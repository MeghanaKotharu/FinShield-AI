# --- verification_orchestrator.py ---
# This service is the main coordinator for the verification process.
# It uses the other services (deepfake, nlp, cross_verifier) to perform a comprehensive analysis.


from fastapi import UploadFile
from app.services.deepfake_service import deepfake_service
from app.services.nlp_service import nlp_service
from app.services.cross_verifier import cross_verifier


class VerificationOrchestrator:
   def process_verification_request(self, text: str = None, file: UploadFile = None) -> dict:
       """
       Orchestrates the entire verification process.


       1. If a file is provided, it runs deepfake analysis and transcribes the text.
       2. It runs NLP analysis on any available text (either provided directly or transcribed).
       3. It performs cross-verification on the claims found in the text.
       4. It calculates a final, consolidated risk score.


       Args:
           text (str, optional): Text input from the user.
           file (UploadFile, optional): File upload from the user.


       Returns:
           dict: A consolidated analysis result.
       """
       final_result = {
           "risk_score": 0,
           "risk_level": "Low",
           "summary": "",
           "deepfake_analysis": None,
           "text_analysis": None,
           "cross_verification": None
       }
      
       analysis_text = text


       # --- Step 1: Process File (if provided) ---
       if file:
           # In a real app, we'd save the file temporarily to pass its path to services
           # For this mock, we just pass the filename.
           file_path = file.filename
           media_analysis = deepfake_service.run_inference(file_path=file_path)
           final_result["deepfake_analysis"] = media_analysis
          
           # Use the transcribed text for content analysis
           if media_analysis.get("transcribed_text"):
               analysis_text = media_analysis["transcribed_text"]
      
       # --- Step 2: Process Text (if available) ---
       if analysis_text:
           text_analysis_result = nlp_service.analyze_text_for_anomalies(analysis_text)
           final_result["text_analysis"] = text_analysis_result


           # --- Step 3: Cross-Verify Claims ---
           if text_analysis_result.get("entities"):
               cross_verification_result = cross_verifier.verify_claims(text_analysis_result["entities"])
               final_result["cross_verification"] = cross_verification_result
      
       # --- Step 4: Calculate Final Risk Score ---
       self._calculate_final_risk(final_result)


       return final_result


   def _calculate_final_risk(self, result: dict):
       """
       Calculates a final risk score based on the consolidated results.
       This is a simple weighted scoring model for the hackathon.
       """
       score = 0
       reasons = []


       # Add points for deepfake confidence
       if result.get("deepfake_analysis") and result["deepfake_analysis"]["is_deepfake"]:
           score += result["deepfake_analysis"]["confidence"] * 50  # Max 50 points
           reasons.append("Media is likely a deepfake.")


       # Add points for NLP flags
       if result.get("text_analysis") and result["text_analysis"]["flags"]:
           score += len(result["text_analysis"]["flags"]) * 15  # 15 points per flag
           reasons.extend(result["text_analysis"]["flags"])


       # Add points for cross-verification failures
       if result.get("cross_verification") and not result["cross_verification"]["is_verified"]:
           score += len(result["cross_verification"]["flags"]) * 25  # 25 points per failed check
           reasons.extend(result["cross_verification"]["flags"])
      
       score = min(score, 100) # Cap score at 100
      
       risk_level = "Low"
       if score > 75:
           risk_level = "Critical"
       elif score > 50:
           risk_level = "High"
       elif score > 25:
           risk_level = "Medium"


       result["risk_score"] = round(score)
       result["risk_level"] = risk_level
       result["summary"] = "Multiple high-risk indicators found." if reasons else "No major risks identified."


# Create a single instance of the orchestrator
verification_orchestrator = VerificationOrchestrator()
