from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from time import time
from app.core.logger import logger

class WatchDogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log the incoming request
        start_time = time()
        
        logger.info(f"Incoming request: {request.method} {request.url}")
        
        # Log request headers (optional)
        # logger.debug(f"Request headers: {dict(request.headers)}")
        
        # Process the request and get the response
        response = await call_next(request)
        
        # Calculate response time
        process_time = time() - start_time
        
        # Log the response details
        logger.info(f"Response status: {response.status_code} | Process time: {process_time:.4f}s")
        
        # Optionally log response headers
        # logger.debug(f"Response headers: {dict(response.headers)}")
        
        return response
