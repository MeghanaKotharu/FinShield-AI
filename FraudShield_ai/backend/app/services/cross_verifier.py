# --- cross_verifier.py ---
# This service is responsible for cross-verifying claims found in text
# against a database of trusted, official information.


class CrossVerifier:
   def __init__(self):
       # In a real implementation, this would connect to a database
       # populated by your data ingestion scripts (from SEBI, BSE, etc.).
       # For the hackathon, we use a simple hardcoded dictionary as a mock database.
       self.mock_official_data = {
           "Innovate Corp": {
               "latest_growth_claim": "25%",
               "official_filings": ["Q3 Report Filed", "AGM Announcement"]
           },
           "FutureTech Ltd": {
               "latest_growth_claim": "15%",
               "official_filings": ["Dividend Declaration"]
           }
       }
       print("Cross Verifier Initialized (using mock database).")


   def verify_claims(self, entities: dict) -> dict:
       """
       Verifies extracted entities against the mock database of official data.


       Args:
           entities (dict): A dictionary of entities extracted by the NLP service,
                            e.g., {"organizations": ["Innovate Corp"], "percentages": ["500%"]}


       Returns:
           dict: A result dictionary indicating if claims are verified and detailing any flags.
       """
       print("Running MOCK cross-verification...")
      
       flags = []
       is_verified = True


       # Check each organization found in the text
       for org in entities.get("organizations", []):
           if org in self.mock_official_data:
               # Check if any percentage claims in the text contradict official data
               for percentage in entities.get("percentages", []):
                   official_claim = self.mock_official_data[org]["latest_growth_claim"]
                   if percentage != official_claim:
                       flags.append(f"Claim Mismatch: '{org}' claim of {percentage} not found. Official record shows {official_claim}.")
                       is_verified = False
           else:
               flags.append(f"Unverified Entity: No official records found for '{org}'.")
               is_verified = False


       if not flags and entities.get("organizations"):
           summary = "All identified claims align with official records."
       elif flags:
           summary = "Discrepancies found between claims and official records."
       else:
           summary = "No specific claims were identified to verify."
           is_verified = True # No claims to dispute, so it's technically verified




       return {
           "is_verified": is_verified,
           "flags": flags,
           "summary": summary
       }


# Create a single instance of the service
cross_verifier = CrossVerifier()
