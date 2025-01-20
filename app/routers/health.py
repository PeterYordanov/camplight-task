#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    The "health" endpoints provide a way to check the responsiveness of our backend and database,
    along with their connectivity.
"""
import os

import asyncpg
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/ping")
def ping():
    """
    A simple endpoint to check the responsiveness of the server.

    Returns:
        str: Returns 'Pong' as a response to a 'ping' request, indicating that the server is responsive.
    """
    return "Pong"


@router.get("/test-database")
async def test_database_connection():
    """
    Tests the database connection using the environment's database URL.

    This endpoint attempts to connect to the database and perform a simple SELECT statement to ensure
    that the connection can be established and is operational.

    Returns:
        dict: A dictionary containing the status of the connection attempt and a message describing the result.

    Raises:
        HTTPException: An error response with status code 500 if the database connection fails,
                       including the error message.
    """
    try:
        conn = await asyncpg.connect(os.getenv("DATABASE_URL"))
        try:
            async with conn.transaction():
                await conn.execute("SELECT 1")
        finally:
            await conn.close()
        return {
            "status": "success",
            "message": "Successfully connected to the database",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
