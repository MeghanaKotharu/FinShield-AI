# --- news_api_client.py ---
# This file contains the logic to connect to a third-party news API
# like NewsAPI.org to fetch general financial news.


import requests
import os
from datetime import datetime


# --- CONFIGURATION ---
# IMPORTANT: It is highly recommended to set your API key as an environment variable
# for security. The code will fall back to the hardcoded key if the variable is not found.
# To get a key, sign up for a free developer plan at https://newsapi.org/
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "7fa48aac1cd84790a63ebb86e8b9cd19")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"


def fetch_general_news():
   """
   Fetches the latest general financial news from the NewsAPI.org service.
   """
   # Safety check: Prevents running the function if the default placeholder key is still present.
   if NEWS_API_KEY == "YOUR_NEWS_API_KEY_HERE":
       print("Warning: NEWS_API_KEY is not set. Skipping general news fetch.")
       return []


   print("Fetching general financial news from NewsAPI.org...")
  
   # Define search parameters for the API call
   params = {
       'q': '"stock market" OR "investment" OR "SEBI" OR "NSE" OR "BSE"', # Search query
       'language': 'en',
       'sortBy': 'publishedAt', # Get the most recent articles
       'pageSize': 10, # Fetch 10 articles
       'apiKey': NEWS_API_KEY
   }


   items = []
   try:
       response = requests.get(NEWS_API_ENDPOINT, params=params)
       response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
      
       articles = response.json().get("articles", [])
      
       for article in articles:
           items.append({
               "source": article['source']['name'],
               "title": article['title'],
               "timestamp": article.get("publishedAt", datetime.utcnow().isoformat() + "Z"),
               "link": article['url'],
               "content": article.get("description", ""),
               "risk_level": "Low", # News from established sources is initially low risk
               "reason": "General News"
           })
          
   except requests.exceptions.RequestException as e:
       print(f"Error fetching data from NewsAPI: {e}")
       # Return an empty list if there's a network or API error
       return []


   print(f"Fetched {len(items)} items from NewsAPI.org.")
   return items


if __name__ == '__main__':
   # This allows you to test this script individually
   print("--- Testing News API Client ---")
   news_data = fetch_general_news()
   if news_data:
       print("Successfully fetched news data. First item:")
       print(news_data[0])
   else:
       print("Could not fetch news data. Is the API key set correctly?")


