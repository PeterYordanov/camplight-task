#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This model is the structure of our input validation for POST and GET requests for the user
"""
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    """
    A Pydantic model that represents a user entity.

    Attributes:
        first_name (Optional[str]): The user's first name. It can be None if not provided.
        last_name (Optional[str]): The user's last name. It can be None if not provided.
        email (Optional[str]): The user's email address. It can be None if not provided.
        phone_number (Optional[str]): The user's telephone number. It can be None if not provided.

    This model is used to validate and structure user data within the system, ensuring consistency and
    reliability of user information throughout the application. It supports optional fields to accommodate
    partial data scenarios, such as when a new user registers without providing all details.

    The Config class within:
        - `orm_mode` is set to True, enabling the model to parse ORM models and treat them as dictionaries,
          which is particularly useful when working with databases using ORMs like SQLAlchemy.
        - `allow_population_by_field_name` allows the model to be populated not just by alias but by actual field names,
          enhancing compatibility between the Pydantic model and ORM models.
    """

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None

    class Config:
        orm_mode = True  # Tells Pydantic to treat the SQLAlchemy model as a dictionary
        allow_population_by_field_name = True
