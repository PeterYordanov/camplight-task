#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from logging import getLogger

import requests

logger = getLogger(__name__)


def fetch_profile_photo():
    """Fetch a profile photo from the thispersondoesnotexist API."""
    try:
        response = requests.get("https://thispersondoesnotexist.com", timeout=10)
        if response.status_code == 200:
            return response.content
        else:
            logger.error(f"Failed to fetch profile photo: {response.status_code}")
            return None
    except Exception as e:
        logger.error(f"Error fetching profile photo: {e}")
        return None
