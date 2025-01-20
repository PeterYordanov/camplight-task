#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    The main driver file that sets up our backend and starts it up
"""

from logging import getLogger

from database.initialize import create_tables, seed_data
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.health import router as health_router
from routers.users import router as user_router

app = FastAPI()
logger = getLogger(__name__)

app.include_router(health_router, prefix="/health", tags=["health", "ping"])
app.include_router(user_router, prefix="/users", tags=["users"])

methods = ["GET", "POST", "PUT", "DELETE"]

headers = ["Authorization", "Content-Type"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # We are in dev, allow all
    allow_methods=methods,
    allow_headers=headers,
)


@app.on_event("startup")
async def startup_event():
    logger.debug("Starting up...")
    create_tables()
    seed_data()
    logger.debug("Startup complete.")
