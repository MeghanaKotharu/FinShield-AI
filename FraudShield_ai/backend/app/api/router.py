# --- router.py ---
# This file includes all the individual endpoint routers into a single main router.


from fastapi import APIRouter
from app.api.endpoints import verification, dashboard


api_router = APIRouter()


# Include the verification endpoint router
api_router.include_router(verification.router, prefix="/verification", tags=["Verification"])


# Include the dashboard endpoint router
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])