# --- run_aggregation_job.py ---
# This is the master script to orchestrate the entire data ingestion process.
# It fetches data from all sources (real and synthetic), consolidates it,
# and saves it to a file that the backend API can serve.


import json
from pathlib import Path
from datetime import datetime


# Import the data fetching functions from other scripts in this directory
from exchange_scraper import fetch_bse_announcements, fetch_sebi_rss
from news_api_client import fetch_general_news


# --- CONFIGURATION ---
# Define the output path for the consolidated data feed.
# This path points to the 'data' directory inside the 'app' folder,
# ensuring the FastAPI server can easily find the file.
OUTPUT_DIR = Path(__file__).parent.parent / "app" / "data"
OUTPUT_FILE = OUTPUT_DIR / "aggregated_feed.json"




def generate_synthetic_social_posts():
   """
   Generates a list of realistic but fake social media posts.
   This is crucial for demonstrating the system's ability to detect high-risk,
   unregulated information.
   """
   print("Generating synthetic social media posts...")
   # In a real app, this could be more dynamic, but for a hackathon,
   # hardcoded examples are clear and effective.
   posts = [
       {
           "source": "Telegram Group",
           "title": "URGENT INSIDER TIP: 'FutureTech Ltd' is about to announce a major breakthrough. Stock will TRIPLE by Friday. Don't miss out! #getrichquick",
           "timestamp": datetime.utcnow().isoformat() + "Z",
           "link": "#",
           "content": "A source deep inside the company confirmed this. This is a guaranteed profit opportunity.",
           "risk_level": "High", # Manually flagged as high risk
           "reason": "Insider Claim, Promissory Language"
       },
       {
           "source": "X (Twitter)",
           "title": "Why is nobody talking about 'Innovate Corp'? Just heard from a friend they have a new risk-free bond offering. Almost too good to be true!",
           "timestamp": datetime.utcnow().isoformat() + "Z",
           "link": "#",
           "content": "Heard from a friend who heard from a guy... sounds legit enough for me. YOLO!",
           "risk_level": "Medium",
           "reason": "Unverified Source, Promissory Language"
       },
       {
           "source": "YouTube Comment",
           "title": "Forget fundamentals, the chart for 'FutureTech Ltd' is screaming buy. We're taking this to the moon! 🚀🚀🚀",
           "timestamp": datetime.utcnow().isoformat() + "Z",
           "link": "#",
           "content": "This is not financial advice, but you'd be a fool to ignore this setup. Big money is moving in.",
           "risk_level": "Medium",
           "reason": "Hype Language"
       }
   ]
   return posts


def run_job():
   """
   Main function to run the entire data aggregation and processing job.
   """
   print(f"--- Starting data aggregation job at {datetime.now()} ---")
  
   all_items = []
  
   # --- STEP 1: Fetch from real sources ---
   # NOTE: fetch_bse_announcements() currently returns mock data for development. See exchange_scraper.py.
   all_items.extend(fetch_bse_announcements())
   all_items.extend(fetch_sebi_rss())
   # This function uses the NewsAPI key to fetch general financial news
   all_items.extend(fetch_general_news())
  
   # --- STEP 2: Generate synthetic data ---
   all_items.extend(generate_synthetic_social_posts())
  
   # --- STEP 3: Ensure output directory exists ---
   OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
  
   # --- STEP 4: Write consolidated data to JSON file ---
   try:
       with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
           json.dump(all_items, f, indent=4, ensure_ascii=False)
       print(f"Successfully wrote {len(all_items)} items to {OUTPUT_FILE}")
   except Exception as e:
       print(f"Error writing to JSON file: {e}")
      
   print(f"--- Data aggregation job finished at {datetime.now()} ---")




if __name__ == "__main__":
   # This allows the script to be run directly from the command line
   # for testing or manual data refreshes.
   run_job()


