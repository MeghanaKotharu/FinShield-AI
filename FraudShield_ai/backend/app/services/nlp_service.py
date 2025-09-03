# --- nlp_service.py ---
# This service handles text analysis using NLP models and rule-based checks.


import re
# You would import your NLP libraries here, e.g.:
# from transformers import pipeline
# import spacy


class NLPService:
   def __init__(self):
       # In a real implementation, you would load your pre-trained NLP model here.
       # This is often done via the Hugging Face transformers library or spaCy.
       # self.sentiment_analyzer = pipeline("sentiment-analysis", model="ProsusAI/finbert")
       # self.ner_model = spacy.load("en_core_web_sm") # Example for NER
       print("NLP Service Initialized (using mock logic).")
       self.suspicious_keywords = ["guaranteed profit", "risk-free", "insider tip", "act now", "urgent"]


   def analyze_text_for_anomalies(self, text: str) -> dict:
       """
       Analyzes the given text for suspicious keywords, sentiment, and key entities.
      
       This is a MOCK function for the hackathon. It performs simple keyword matching and regex for entity extraction.
       In a real implementation, this function would:
       1. Use a pre-trained model like FinBERT for sentiment analysis.
       2. Use a proper NER model (like from spaCy or FinBERT) to extract company names, monetary values, and percentages.
       3. Combine model output with rule-based checks.
       """
       print("Running MOCK NLP analysis with entity extraction...")
      
       flags = []
       text_lower = text.lower()
      
       # --- Keyword Analysis ---
       for keyword in self.suspicious_keywords:
           if keyword in text_lower:
               if keyword in ["guaranteed profit", "risk-free"]:
                   flags.append("Promissory Language")
               elif keyword in ["insider tip"]:
                   flags.append("Insider Claim")
               elif keyword in ["act now", "urgent"]:
                   flags.append("Urgency Pressure")
      
       # --- Mock Entity Extraction (NER) ---
       # A real implementation would use a spaCy or Hugging Face model here.
       # This regex is a simple placeholder for the hackathon.
       extracted_orgs = re.findall(r"'([A-Z][A-Za-z\s]+Corp)'", text) # Finds words like 'Innovate Corp'
       extracted_percentages = re.findall(r'(\d+\s*%)', text) # Finds numbers followed by %


       entities = {
           "organizations": list(set(extracted_orgs)),
           "percentages": list(set(extracted_percentages))
       }


       # --- Mock Sentiment Analysis ---
       sentiment = "Positive" if "profit" in text_lower or "growth" in text_lower else "Neutral"
      
       # --- Final Summary ---
       summary = "Text contains high-risk language and pressure tactics." if flags else "Text appears to be standard."
       if entities["organizations"] or entities["percentages"]:
           summary += f" Key claims identified regarding {', '.join(entities['organizations'])}."


       return {
           "sentiment": sentiment,
           "flags": list(set(flags)), # Use set to remove duplicates
           "entities": entities,
           "summary": summary
       }


# Create a single instance of the service
nlp_service = NLPService()