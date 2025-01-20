#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This model specifies input validation for the pagination parameters (Specifically for the GET endpoint)
"""
from pydantic import BaseModel, Field


class PaginationParams(BaseModel):
    """
    A Pydantic model that defines the parameters for pagination in API requests.

    Attributes:
        page (int): The current page number in the pagination sequence, starting from 1. It must be at least 1.
        page_size (int): The number of items to display per page. It must be between 1 and 100, inclusive.

    This model is utilized to ensure that API requests conform to the pagination standards set forth in the application,
    providing clients with consistent and manageable chunks of data. The validation constraints ensure that the page
    number and page size are within acceptable limits, preventing errors in data retrieval or display.

    Usage:
        - `page` helps in fetching a specific segment of the dataset.
        - `page_size` controls the volume of data returned, helping to optimize load times and manageability.

    The fields are accompanied by default values and constraints to guide the user and validate inputs effectively.
    """

    page: int = Field(
        default=1,
        ge=1,
        description="Page number starting from 1",
        example=1,
        errors={"ge": "Page must be greater than or equal to 1"},
    )
    page_size: int = Field(
        default=10,
        ge=1,
        le=100,
        description="Number of items per page, max 100",
        example=10,
        errors={
            "ge": "Page size must be at least 1",
            "le": "Page size must not exceed 100",
        },
    )
