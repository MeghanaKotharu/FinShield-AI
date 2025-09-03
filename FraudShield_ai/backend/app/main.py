# --- main.py ---
# This is the main entry point for our application.
# To run this server, navigate to the `backend/` directory in the terminal
# and run the command: uvicorn app.main:app --reload


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.api.router import api_router


# Create the main FastAPI application instance
app = FastAPI(
   title="MarketGuard AI API",
   description="API for detecting deepfakes and analyzing financial announcements.",
   version="1.0.0"
)


# --- CORS (Cross-Origin Resource Sharing) Middleware ---
# This is crucial for allowing your React frontend (running on a different port, e.g., 3000)
# to communicate with this backend server (running on port 8000).
app.add_middleware(
   CORSMiddleware,
   allow_origins=["http://localhost:3000"],  # Allows your React app
   allow_credentials=True,
   allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
   allow_headers=["*"],  # Allows all headers
)


# --- API Router ---
# Include the main router from `app/api/router.py`.
# This router contains all the specific endpoints (e.g., /verify, /dashboard_feed).
app.include_router(api_router, prefix="/api")


# --- Root Endpoint ---
# A simple endpoint to check if the server is running.
@app.get("/", tags=["Health Check"])
def read_root():
   return {"status": "MarketGuard AI server is running"}






