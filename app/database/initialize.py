#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This file focuses on the creation of tables and seed data in the event that our database is empty
"""
import os
from logging import getLogger

from database.tables import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
logger = getLogger(__name__)


def create_tables():
    """
    Create database tables based on predefined SQLAlchemy Base metadata.

    This function utilizes the SQLAlchemy ORM's declarative base to reflect the schema
    definitions onto the connected database. It should be called at the initial setup
    phase of the application to ensure that the database schema is correctly set up.

    Requires:
        An already defined SQLAlchemy ORM `Base` with entity declarations and
        a global `engine` object connected to the desired database.
    """
    Base.metadata.create_all(engine)


def seed_data():
    """
    Seed the database with initial data if no data exists.

    This function checks for existing user data and seeds the database with predefined
    user entries if the user table is empty. It is intended to be used during the initial
    setup phase or when resetting the database to a default state.

    Side Effects:
        - Adds multiple `User` entries to the database if it is initially empty.
        - Commits transactions to the database.
        - Rolls back transactions in case of an error.

    Error Handling:
        Logs errors to a logger and rolls back the session if an error occurs during
        the database transactions.
    """
    try:
        with Session(engine) as session:
            existing_users = session.query(User).all()

            if not existing_users:
                seed_users = [
                    User(
                        first_name="Alex",
                        last_name="Taylor",
                        email="alex.taylor@example.com",
                        phone_number="1234567890",
                    ),
                    User(
                        first_name="Jordan",
                        last_name="Lee",
                        email="jordan.lee@example.com",
                        phone_number="0987654321",
                    ),
                    User(
                        first_name="Casey",
                        last_name="Morgan",
                        email="casey.morgan@example.com",
                        phone_number="1122334455",
                    ),
                    User(
                        first_name="Taylor",
                        last_name="Parker",
                        email="taylor.parker@example.com",
                        phone_number="2233445566",
                    ),
                    User(
                        first_name="Morgan",
                        last_name="Reed",
                        email="morgan.reed@example.com",
                        phone_number="3344556677",
                    ),
                    User(
                        first_name="Riley",
                        last_name="Adams",
                        email="riley.adams@example.com",
                        phone_number="4455667788",
                    ),
                    User(
                        first_name="Cameron",
                        last_name="Blake",
                        email="cameron.blake@example.com",
                        phone_number="5566778899",
                    ),
                    User(
                        first_name="Quinn",
                        last_name="Hayes",
                        email="quinn.hayes@example.com",
                        phone_number="6677889900",
                    ),
                ]

                session.add_all(seed_users)
                session.commit()
                logger.info("Database seeded successfully.")
            else:
                logger.info("Database already has data. Skipping seeding.")
    except Exception as e:
        logger.error(f"Error seeding the database: {str(e)}")
        session.rollback()
