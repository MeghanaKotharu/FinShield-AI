# --- exchange_scraper.py ---
# This file contains functions to fetch data from specific, legitimate sources
# like official exchange websites or RSS feeds.


import feedparser
from datetime import datetime


def fetch_bse_announcements():
   """
   Fetches the latest corporate announcements from the BSE India's public RSS feed.
   This is the REAL implementation.
   """
   print("Fetching real-time data from BSE India RSS feed...")
   # The official URL for BSE's corporate announcement RSS feed
   bse_rss_url = "https://www.bseindia.com/corporates/ann.xml"
  
   items = []
   try:
       # Use feedparser to fetch and parse the XML feed
       feed = feedparser.parse(bse_rss_url)
      
       # Loop through the first 10 entries to get the latest announcements
       for entry in feed.entries[:10]:
           items.append({
               "source": "BSE India",
               "title": entry.title,
               "timestamp": entry.get("published", datetime.utcnow().isoformat() + "Z"),
               "link": entry.link,
               "content": entry.get("summary", ""),
               "risk_level": "Low", # Data from official sources is initially considered low risk
               "reason": "Standard Filing"
           })
   except Exception as e:
       print(f"Error fetching BSE RSS feed: {e}")
       # Return an empty list if there's an error to prevent the job from crashing
       return []


   print(f"Fetched {len(items)} items from BSE.")
   return items


def fetch_sebi_rss():
   """
   Fetches the latest press releases from SEBI's public RSS feed.
   """
   print("Fetching data from SEBI RSS feed...")
   sebi_rss_url = "https://www.sebi.gov.in/sebirss.xml"
  
   items = []
   try:
       feed = feedparser.parse(sebi_rss_url)
       for entry in feed.entries[:5]: # Get latest 5 entries
           items.append({
               "source": "SEBI",
               "title": entry.title,
               "timestamp": entry.get("published", datetime.utcnow().isoformat() + "Z"),
               "link": entry.link,
               "content": entry.get("summary", ""),
               "risk_level": "Low", # Official notices are generally low risk
               "reason": "Official Advisory"
           })
   except Exception as e:
       print(f"Error fetching SEBI RSS feed: {e}")


   print(f"Fetched {len(items)} items from SEBI.")
   return items


if __name__ == '__main__':
   # This allows you to test this script individually
   print("--- Testing BSE Scraper ---")
   bse_data = fetch_bse_announcements()
   # Print the title of the first item if data was fetched
   if bse_data:
       print("Successfully fetched BSE data. First item:")
       print(bse_data[0])
   else:
       print("Could not fetch BSE data.")
  
   print("\n--- Testing SEBI Scraper ---")
   sebi_data = fetch_sebi_rss()
   if sebi_data:
       print("Successfully fetched SEBI data. First item:")
       print(sebi_data[0])
   else:
       print("Could not fetch SEBI data.")
