#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from sqlalchemy import Column, Integer, LargeBinary, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    Represents a user entity within the database with a corresponding 'users' table.

    Attributes:
        id (int): The primary key that uniquely identifies the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email address of the user, which must be unique.
        phone_number (str): The contact phone number of the user.
        profile_photo (bytes, optional): A binary large object that can store the user's profile photo.

    The `User` model includes standard attributes for managing user information. The `email` field is
    unique to prevent duplicate entries. The `profile_photo` field is optional and can store binary data,
    suitable for saving images or other binary formats directly in the database.

    Table:
        - The SQLAlchemy `__tablename__` attribute explicitly names the database table used to store `User` records.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    profile_photo = Column(LargeBinary, nullable=True)
